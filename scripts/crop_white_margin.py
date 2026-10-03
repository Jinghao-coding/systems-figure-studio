#!/usr/bin/env python3
"""Crop uniform near-white raster margins while retaining a safety margin."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops


def bounded_byte(value: str) -> int:
    number = int(value)
    if not 0 <= number <= 255:
        raise argparse.ArgumentTypeError("must be between 0 and 255")
    return number


def nonnegative_int(value: str) -> int:
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be non-negative")
    return number


def composite_on_white(image: Image.Image) -> Image.Image:
    """Flatten every input mode onto white so transparent pixels stay empty."""

    foreground = image.convert("RGBA")
    background = Image.new("RGBA", foreground.size, (255, 255, 255, 255))
    return Image.alpha_composite(background, foreground).convert("RGB")


def find_content_bbox(image: Image.Image, threshold: int) -> tuple[int, int, int, int] | None:
    """Return pixels where any RGB channel is below the near-white threshold."""

    red, green, blue = image.split()
    deviation = ImageChops.lighter(ImageChops.invert(red), ImageChops.invert(green))
    deviation = ImageChops.lighter(deviation, ImageChops.invert(blue))
    cutoff = 255 - threshold
    mask = deviation.point(lambda value: 255 if value > cutoff else 0)
    return mask.getbbox()


def crop_near_white(
    image: Image.Image, margin: int = 16, threshold: int = 248
) -> tuple[Image.Image, tuple[int, int, int, int]]:
    """Return a white-flattened crop and the expanded source-space crop box."""

    if margin < 0:
        raise ValueError("margin must be non-negative")
    if not 0 <= threshold <= 255:
        raise ValueError("threshold must be between 0 and 255")

    flattened = composite_on_white(image)
    bbox = find_content_bbox(flattened, threshold)
    if bbox is None:
        raise ValueError("no non-white content found")

    left, top, right, bottom = bbox
    box = (
        max(0, left - margin),
        max(0, top - margin),
        min(flattened.width, right + margin),
        min(flattened.height, bottom + margin),
    )
    return flattened.crop(box), box


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Crop uniform near-white raster margins without editing semantics."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--margin",
        type=nonnegative_int,
        default=16,
        help="safety margin to retain in pixels (default: 16)",
    )
    parser.add_argument(
        "--threshold",
        type=bounded_byte,
        default=248,
        help="RGB channels at or above this value count as near-white (default: 248)",
    )
    args = parser.parse_args()

    with Image.open(args.input) as source:
        original_size = source.size
        try:
            cropped, box = crop_near_white(source, args.margin, args.threshold)
        except ValueError as error:
            parser.exit(2, f"error: {error}\n")
        save_metadata = {
            key: source.info[key]
            for key in ("dpi", "icc_profile")
            if key in source.info
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    cropped.save(args.output, **save_metadata)
    print(f"{original_size[0]}x{original_size[1]} -> {cropped.width}x{cropped.height}; box={box}")


if __name__ == "__main__":
    main()
