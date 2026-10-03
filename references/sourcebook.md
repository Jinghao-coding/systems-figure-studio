# 来源与视觉取舍

R 开头为已迁移的原图模式，AG 为保留的 Agent 记录，S 为本轮非 Agent 补充。原图已看过、局部可以借鉴、改编图已生成分别记录。引用只支持本条注明的关系，不为每个原创画法背书。原图不随包打包，读者可通过来源访问。

<a id="r01"></a>

## R01 · 收窄—展开的低秩支路

**来源：** [LoRA](https://arxiv.org/pdf/2106.09685)；ICLR 2022 / 预印本图。  
**版本／范围：** arXiv v2（2021-10）；不是对最终排版版本的逐像素核对；Fig. 1；PDF 页 1。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 主权重使用宽面；旁路由两个方向相反的梯形组成，中间明显收窄；上下向量通过加法汇合。

**值得保留：** 保留宽—窄—宽轮廓、独立旁路和加法节点；可旋转布局，不改变维度映射。

**需要取舍：** 不要把梯形解释为模型规模变化；不能删掉主路或把两路串联。

**原图入口：** [查看原图](https://ar5iv.labs.arxiv.org/html/2106.09685/assets/x1.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r02"></a>

## R02 · 斜置、多尺度的特征平面

**来源：** [Feature Pyramid Networks](https://arxiv.org/pdf/1612.03144)；CVPR 2017。  
**版本／范围：** 作者预印本对应图；Fig. 1；PDF 页 1。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 不同大小的斜置平面叠成尺度层次；图中并列四种连接布局，底部可保留图像内容。

**值得保留：** 保留平面倾角、逐级尺度变化、横向/纵向路径；不把平面替换为写着 feature 的等大框。

**需要取舍：** 平面面积在这里关联空间尺度；不能无说明当显存或参数量。

**原图入口：** [查看原图](https://ar5iv.labs.arxiv.org/html/1612.03144/assets/x1.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r03"></a>

## R03 · 图—层叠平面—图—小网络

**来源：** [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/)；Distill 2021。  
**版本／范围：** 作者博客原图；端到端 GNN 示意图；PDF 页 None。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 不规则节点图穿过倾斜的网络层平面；输出仍是节点图，再接圆节点的小型分类网络。

**值得保留：** 保留输入/输出拓扑对应、平面层次、圆节点网络；只裁取所需局部。

**需要取舍：** 层平面不是模型副本；没有 pooling 时不能擅自减少节点。

**原图入口：** [查看原图](https://distill.pub/2021/gnn-intro/Overall.e3af58ab.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r04"></a>

## R04 · 状态主干与门控支路

**来源：** [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)；Chris Olah 2015。  
**版本／范围：** 作者博客原图；展开的 LSTM 链；PDF 页 None。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 连续状态主干穿过重复单元；中间单元展开，圆形乘加节点和弯曲支路连接学习变换。

**值得保留：** 保留贯穿主干、重复单元、分流/汇流和局部展开；非焦点单元减弱。

**需要取舍：** 不要把 LSTM 的乘加门控照搬成 Agent 推理内部结构；借用布局时须标改编。

**原图入口：** [查看原图](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-chain.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r05"></a>

## R05 · 操作与数据路径的形状语法

**来源：** [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)；Chris Olah 2015。  
**版本／范围：** 作者博客原图；图形符号说明；PDF 页 None。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 学习层、逐元素运算、向量传递、拼接和复制分支使用不同符号。

**值得保留：** 小圆圈用于明确的运算，向量沿路径移动；分支与拼接各有连接结构。

**需要取舍：** 图形语法是该文章的约定；迁移后仍需图例，不把所有汇合默认为加法。

**原图入口：** [查看原图](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM2-notation.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r06"></a>

## R06 · 带分量的嵌入向量

**来源：** [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)；Jay Alammar 2018。  
**版本／范围：** 作者博客原图；Embedding 图；PDF 页 None。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 词上方是带分格的窄向量带，空间对应关系直接连接词与数值表示。

**值得保留：** 保留分量节奏和词—向量的一一对应；分格数量作为示意说明。

**需要取舍：** 不能用实际示意格数声称 embedding 维度，也不能把每格当一个 token。

**原图入口：** [查看原图](https://jalammar.github.io/images/t/embeddings.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r07"></a>

## R07 · 展开一层，折叠重复层

**来源：** [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/)；Jay Alammar 2019。  
**版本／范围：** 作者博客原图；Decoder block vectors；PDF 页 None。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 多层 decoder 竖向排列，底层展开 attention 与前馈结构；向量沿路径贯穿。

**值得保留：** 保留层叠节奏、一个展开层和连续 token 路径；其余用省略号压缩。

**需要取舍：** 层数不能暗示实例数；用作不透明模型概览时不要虚构具体层配置。

**原图入口：** [查看原图](https://jalammar.github.io/images/gpt2/gpt2-transformer-block-vectors-2.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r08"></a>

## R08 · 向量束的加权汇聚

**来源：** [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/)；Jay Alammar 2019。  
**版本／范围：** 作者博客所引用路径中的原图；Self-attention weighted values；PDF 页 None。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 平行向量束分别经过圆形乘法点；加权结果汇成一个输出向量。

**值得保留：** 保留多路向量、各自权重和最后求和；路径有清晰对应。

**需要取舍：** 向量变淡必须说明含义；不能把 attention 权重当专家占用率。

**原图入口：** [查看原图](https://jalammar.github.io/images/xlnet/self-attention-3-2.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r09"></a>

## R09 · 概率条与选择性专家路径

**来源：** [Switch Transformers](https://jmlr.org/papers/volume23/21-0998/21-0998.pdf)；JMLR 2022。  
**版本／范围：** JMLR 图面已核对；展示图像来自对应 ar5iv 转换；Fig. 2；PDF 页 4。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 输入 token 带、路由概率小柱、专家行、选中实线和门控虚线共同构成局部放大图。

**值得保留：** 保留概率分布、选中路径、未选专家与残差绕行；提取结构而非复制外框。

**需要取舍：** 本图是单专家 Switch 路由；改成 Top-k 必须明确新增语义。

**原图入口：** [查看原图](https://ar5iv.labs.arxiv.org/html/2101.03961/assets/x3.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r10"></a>

## R10 · token 置换与容量留白

**来源：** [Switch Transformers](https://jmlr.org/papers/volume23/21-0998/21-0998.pdf)；JMLR 2022。  
**版本／范围：** JMLR 图面已核对；展示图像来自对应 ar5iv 转换；Fig. 3；PDF 页 5。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 一组细长 token 柱被分配到上方多个专家；跨设备连线保留身份，空位和溢出不同。

**值得保留：** 保留长条 token 身份、目标边界、未填空间和明确溢出支路。

**需要取舍：** 空闲专家容量不是通用 GPU 显存；容量因子例子不能泛化为硬件配置。

**原图入口：** [查看原图](https://ar5iv.labs.arxiv.org/html/2101.03961/assets/x4.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r11"></a>

## R11 · 沙漏轮廓与迭代回路

**来源：** [High-Resolution Image Synthesis with Latent Diffusion Models](https://ommer-lab.com/research/latent-diffusion-models/)；CVPR 2022。  
**版本／范围：** 作者项目页对应论文图；Fig. 3；PDF 页 None。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 编码/解码使用相反的梯形；U-Net 使用中间收窄的双翼轮廓；条件路径接入内部，多步去噪通过回路表达。

**值得保留：** 保留像素/潜空间分界、压缩与展开方向、跨层连接及迭代次数标记。

**需要取舍：** 沙漏仅在确有编码解码层次时使用；噪声变化不是训练收敛曲线。

**原图入口：** [查看原图](https://ommer-lab.com/wp-content/uploads/2022/08/article-Figure3-1-1024x508.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r12"></a>

## R12 · 时间展开的图结构

**来源：** [Spatial Temporal Graph Convolutional Networks](https://arxiv.org/pdf/1801.07455)；AAAI 2018。  
**版本／范围：** 作者预印本对应图；Fig. 2；PDF 页 3。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 视频帧叠放后转为多时刻骨架图层；同一关节跨时间相连，局部感受野着色。

**值得保留：** 保留重复对象的稳定位置、时序连接和局部高亮范围；可借作时序图结构表达。

**需要取舍：** 时间层不能与神经网络深度混用；高亮面不是物理覆盖区域。

**原图入口：** [查看原图](https://ar5iv.labs.arxiv.org/html/1801.07455/assets/x1.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r13"></a>

## R13 · 特征片—查询集合—匹配弧线

**来源：** [End-to-End Object Detection with Transformers](https://arxiv.org/pdf/2005.12872)；ECCV 2020。  
**版本／范围：** 作者预印本对应图；Fig. 2；PDF 页 7。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 锥形 CNN、叠置位置特征、token 行和带身份的查询点并列，输出用弧线连接至不同预测头。

**值得保留：** 保留查询身份、弧线端点、特征平面和检测框对应；可裁成小型查询模块。

**需要取舍：** 查询集合不能暗示 FCFS 顺序；整图大框并非所有组件的推荐外形。

**原图入口：** [查看原图](https://ar5iv.labs.arxiv.org/html/2005.12872/assets/x2.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r14"></a>

## R14 · 图像切片展开成序列

**来源：** [An Image is Worth 16x16 Words](https://arxiv.org/pdf/2010.11929)；ICLR 2021。  
**版本／范围：** 作者预印本对应图；Fig. 1；PDF 页 3。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 图像网格被拆到一排可辨识的 patch 缩略片；上方对应嵌入与位置标记，旁边展开 encoder。

**值得保留：** 保留二维到一维的对应、图像纹理、独立 class token；按需要裁局部。

**需要取舍：** 网格数量不代表真实模型配置；不要把 patch、token 与向量分量混为一类。

**原图入口：** [查看原图](https://ar5iv.labs.arxiv.org/html/2010.11929/assets/x1.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r15"></a>

## R15 · 稀疏输入与双路网络

**来源：** [DeepFM](https://www.ijcai.org/proceedings/2017/0239.pdf)；IJCAI 2017。  
**版本／范围：** IJCAI PDF 页码以当前文件为准；图像另取作者预印本；Fig. 1；PDF 页 None。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 字段分组的稀疏圆点经共享 embedding 接到 FM 和 DNN 两条分支；节点内运算符可辨。

**值得保留：** 保留字段边界、共享嵌入层、分叉和运算节点；抽取局部减少密集连线。

**需要取舍：** 不要把共享 embedding 画成两个独立参数副本。

**原图入口：** [查看原图](https://ar5iv.labs.arxiv.org/html/1703.04247/assets/img/architecture-deepfm.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r16"></a>

## R16 · 字段内的稀疏到稠密扇入

**来源：** [DeepFM](https://ar5iv.labs.arxiv.org/html/1703.04247)；IJCAI 2017。  
**版本／范围：** 作者预印本原图；Fig. 4；PDF 页 None。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 底部字段中的少量激活圆点，通过局部扇入连接到同宽的 embedding 节点行。

**值得保留：** 保留每个字段独立映射、输入激活和输出等宽；可替换字段名。

**需要取舍：** 连线表示权重映射，不能当网络设备的物理全互连。

**原图入口：** [查看原图](https://ar5iv.labs.arxiv.org/html/1703.04247/assets/img/embedding.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="r17"></a>

## R17 · 计算阵列与单元剖面

**来源：** [Eyeriss](https://eems.mit.edu/wp-content/uploads/2016/04/eyeriss_isca_2016.pdf)；ISCA 2016。  
**版本／范围：** 作者托管论文 PDF；Fig. 1；PDF 页 2。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 阵列内有重复 PE 与互连；外接缓冲/FIFO；引出线展开单个 PE 的 ALU 多边形、RF 和路径。

**值得保留：** 保留重复结构、局部剖面、特殊运算形体和分层存储；不用孤立芯片剪影代替。

**需要取舍：** 该结构属于特定 CNN 加速器，不能冒充 NVIDIA GPU 实际 floorplan。

<a id="r18"></a>

## R18 · 交叉网络与归约树装进执行单元

**来源：** [SIGMA](https://anands09.github.io/papers/sigma_hpca2020.pdf)；HPCA 2020。  
**版本／范围：** 作者托管论文 PDF；Fig. 5；PDF 页 6。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** Flex-DPE 中排列多级交叉线网、乘法阵列和归约树；旁边矩阵映射解释数据去向。

**值得保留：** 保留内部三段结构、端点对齐、选中路径；装置边界包住拓扑而非取代拓扑。

**需要取舍：** 逻辑互连不等于任意 GPU 的片上布局；复制此形体必须保留抽象层说明。

<a id="r19"></a>

## R19 · 存储层级与分块流动

**来源：** [FlashAttention](https://arxiv.org/pdf/2205.14135)；NeurIPS 2022。  
**版本／范围：** 作者预印本原图；Fig. 1；PDF 页 2。  
**审阅状态：** 2026-10-02 重新查看实际 PDF 图面；来源审阅与本次改编图认可分开。

**观察或依据：** 层次金字塔与矩阵切块视图并列；Q/K/V 条带围绕虚线计算平面，移动块沿路径进入局部计算。

**值得保留：** 分开裁取存储层级或 tile 流动；保留块边界和路径，不带原性能数值。

**需要取舍：** 金字塔不按面积解释容量；虚线得分平面不表示完整矩阵已写入 HBM。

**原图入口：** [查看原图](https://ar5iv.labs.arxiv.org/html/2205.14135/assets/x1.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

**本次取舍：** 借鉴不同形体区分存储位置与计算tile、细线连接实际搬移端点；原图红绿强调较密，不照搬配色。此图不提供GPU板卡外观依据。

<a id="r20"></a>

## R20 · 多级汇总的形状分工

**来源：** [Decima](https://web.mit.edu/decima/content/sigcomm-2019.pdf)；SIGCOMM 2019。  
**版本／范围：** 作者托管论文 PDF；Fig. 5；PDF 页 5。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 相同作业小图多次出现；节点、作业汇总和全局汇总有不同形状与扇入连线。

**值得保留：** 保留 DAG 内部结构、汇总层次和稳定身份；只摘取一条汇总链。

**需要取舍：** 三角形不是全领域统一的 embedding 符号，必须注明层级含义。

<a id="r21"></a>

## R21 · 请求内部的长短 token 行

**来源：** [Orca](https://www.usenix.org/system/files/osdi22-yu.pdf)；OSDI 2022。  
**版本／范围：** USENIX 正式 PDF；页码包含封面；Fig. 4；PDF 页 6。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 请求池中的每个请求包含不同长度的 token 行；输入和已生成 token 有区分。

**值得保留：** 保留请求身份与内部内容，按迭代只更新新 token；裁掉无关模块外框。

**需要取舍：** 本例顺序不是全部场景的 FCFS 承诺；分量格和 token 格不能混淆。

<a id="r22"></a>

## R22 · 逻辑页—映射记录—物理页

**来源：** [PagedAttention / vLLM](https://arxiv.org/pdf/2309.06180)；SOSP 2023。  
**版本／范围：** 作者预印本原图；Fig. 6–7；PDF 页 6。  
**审阅状态：** 2026-10-02 重新查看实际 PDF 图面；来源审阅与本次改编图认可分开。

**观察或依据：** 请求圆标对应逻辑页格，经中间映射记录指向不连续的物理页；两请求共享一个物理视图。

**值得保留：** 保留块内 token、映射端点、空位和请求身份；不能简化成 Memory 字框。

**需要取舍：** 逻辑相邻不代表物理相邻；不要把不同请求同色等同共享同一 KV。

**本次取舍：** 页内保留词元内容或分格，使状态页区别于没有粒度的空方块；概览可省映射表细目，解释分页机制时则保留逻辑与物理两侧及映射。

<a id="r23"></a>

## R23 · 前缀树的连续状态

**来源：** [SGLang 正式论文](https://papers.nips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf)；NeurIPS 2024。  
**版本／范围：** 正式会议版本 Fig. 3；PDF 页 5。早期预印本 Fig. 6 的记录由此次正式版核对更新。  
**审阅状态：** 2026-10-02 实际查看正式版 PDF 图面；未据此认定改编图已获用户认可。

**观察或依据：** 树的公共前缀、分裂、新增和驱逐在九个时刻保持可追踪；驱逐位置以退出痕迹说明。

**值得保留：** 保留公共主干、分支身份和变化事件；概览只取三四帧，正文再展开。

**需要取舍：** 正式版图号为 3，与早期展示版本的 6 区分；请求完成不必清空前缀缓存。

**原图入口：** [查看原图](https://ar5iv.labs.arxiv.org/html/2312.07104/assets/x6.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

**本次取舍：** 提炼固定节点身份、细折线树和少量状态强调，避免为每帧增加大外框；不把九帧和长对话标签整体复制到概览图。

<a id="r24"></a>

## R24 · 按 rank 保留比例的状态条

**来源：** [ZeRO](https://arxiv.org/pdf/1910.02054)；SC 2020。  
**版本／范围：** 作者预印本原图；Fig. 1；PDF 页 3。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 参数、梯度和优化器状态使用分层条带；不同 rank 对齐；不同阶段保留或切分对应部分。

**值得保留：** 保留三种状态的层次与跨 rank 一致标尺；重画时删掉原实验数值。

**需要取舍：** 条带长度代表示例容量而非时间；切片不等于完整副本。

<a id="r25"></a>

## R25 · 长 prefill 与短 decode 的执行节奏

**来源：** [Sarathi-Serve](https://www.usenix.org/system/files/osdi24-agrawal.pdf)；OSDI 2024。  
**版本／范围：** USENIX 正式 PDF；页码包含封面；Fig. 7；PDF 页 7。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 同一组请求在四条策略时间线中重复；长块、短块、分块和显式停顿形成不同节奏。

**值得保留：** 保留相同事件起点、请求身份、阶段长短、入场/退出；不是等长框串。

**需要取舍：** 这里只描述论文当时比较，不当作当前 vLLM 的行为说明。

<a id="r26"></a>

## R26 · 节点内重复设备与占用

**来源：** [Tiresias](https://www.usenix.org/system/files/nsdi19-gu.pdf)；NSDI 2019。  
**版本／范围：** USENIX 正式 PDF；页码包含封面；Fig. 6；PDF 页 5。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** GPU 集群以机器单元重复，单元内含四个设备格，实填/空白表示占用。

**值得保留：** 只保留集群局部的两层归属与占用；其他类不必沿用格子。

**需要取舍：** 每机器四卡是图中示例；该图形适合容量，不作为形体多样性的唯一范本。

<a id="r27"></a>

## R27 · 逻辑到执行的工作流层次

**来源：** [Murakkab](https://www.usenix.org/system/files/osdi26-chaudhry.pdf)；OSDI 2026。  
**版本／范围：** USENIX 正式 PDF；官网录用/发表信息已核对；Fig. 5；PDF 页 7。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 逻辑工作流、优化后的分支结构与具体执行资源在连续阶段间对应。

**值得保留：** 保留小型 DAG 的变化及任务—资源对应；去掉人物、锤子等与机制无关的装饰。

**需要取舍：** 只借鉴对应关系，不把此系统的机制强加到待画系统。

<a id="r28"></a>

## R28 · 计算格点与遍历路径

**来源：** [FlexGen](https://proceedings.mlr.press/v202/sheng23a/sheng23a.pdf)；ICML 2023。  
**版本／范围：** PMLR 正式 PDF；Fig. 2；PDF 页 4。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 计算对象放在具有 batch、layer、token 含义的格点结构中。

**值得保留：** 保留轴的含义与计算顺序；只为解释遍历使用格点，不能泛化为全部对象模板。

**需要取舍：** 这是一种有语义的网格，不是避免方块的形体范本。

<a id="r29"></a>

## R29 · Agent 与记忆、工具和规划的组织

**来源：** [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)；Lilian Weng 2023。  
**版本／范围：** 作者博客原图；主动筛除形体层面的误用；Agent overview；PDF 页 None。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 原图主要仍是带文字的模块矩形，展示中心 Agent 与记忆、工具、规划、行动的关系。

**值得保留：** 仅用于组织层次参考；具体 Agent、记忆和工具小组件需要另配图形。

**需要取舍：** 不能因为博客经典就把该图宣传成多样化形体范本。

**原图入口：** [查看原图](https://lilianweng.github.io/posts/2023-06-23-agent/agent-overview.png)（依赖来源可访问性；不等于已向生图模型提供图像）。

<a id="ag01"></a>

## AG01 · AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

**来源：** [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/pdf/2308.08155v2)；arXiv / 按记录版本。  
**版本／范围：** 2308.08155v2；Fig. 1; Fig. 3；PDF 页 [1, 6]。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 小机器人头像配能力徽标；通过同族对象的连线形成联合对话、层级协作与动态群聊。对话内容使用气泡，角色身份与消息形态分开。

**值得保留：** 角色头像＋能力条；对话气泡；同一套图元复用于不同协作拓扑。

**需要取舍：** 减少灰底大容器和高密度小图标。能力徽标可改成通用短标签，不照搬品牌。

<a id="ag02"></a>

## AG02 · GPTSwarm: Language Agents as Optimizable Graphs

**来源：** [GPTSwarm: Language Agents as Optimizable Graphs](https://arxiv.org/pdf/2402.16823v3)；arXiv / 按记录版本。  
**版本／范围：** 2402.16823v3；Fig. 1；PDF 页 [2]。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 用不同形状的操作节点组成单个 Agent 的局部图，再将各 Agent 小图连接为群体网络；角落的角色形象标记 Agent 身份。

**值得保留：** 操作—局部图—群体图的尺度层次；局部展开；跨 Agent 的通信边。

**需要取舍：** 去掉贯穿画面的彩虹渐变、棋盘纹理、冗余 Logo、厚阴影；不要把饱满装饰当成结构。

<a id="ag03"></a>

## AG03 · Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks

**来源：** [Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks](https://arxiv.org/pdf/2411.04468v1)；arXiv / 按记录版本。  
**版本／范围：** 2411.04468v1；Fig. 1；PDF 页 [1]。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 角色用文件、代码、终端、浏览器等小符号识别；编号执行步骤下摆放相应代码、浏览器或终端产物。

**值得保留：** 角色图标＋实际产物；步骤编号；同一角色在多个时刻重复出现。

**需要取舍：** 压缩截图文字，简化长距离虚线路径；不能把步骤重复误画成新增 Agent。

<a id="ag04"></a>

## AG04 · AFlow: Automating Agentic Workflow Generation

**来源：** [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/pdf/2410.10762v4)；arXiv / 按记录版本。  
**版本／范围：** 2410.10762v4；Fig. 2；PDF 页 [4]。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 圆节点及颜色区分操作；扇入结构表现 ensemble，局部反馈与条件节点表现 debate 和 self-refine；另列节点配置与代码/图等关系表示。

**值得保留：** 可复用小拓扑：生成—评审—修改回路、并行候选—汇总、带历史状态的局部交互。

**需要取舍：** 降低粗边框和投影，少用多层虚线卡片。节点不自动等于独立 Agent 或模型实例。

<a id="ag05"></a>

## AG05 · Agent Lightning: Train ANY AI Agents with Reinforcement Learning

**来源：** [Agent Lightning: Train ANY AI Agents with Reinforcement Learning](https://arxiv.org/pdf/2508.03680v1)；arXiv / 按记录版本。  
**版本／范围：** 2508.03680v1；Fig. 1；PDF 页 [2]。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 左侧是 Agent、工具和小网络；上方弧线把训练轨迹送向训练引擎，下方反向弧线返回更新模型。

**值得保留：** 执行侧与训练侧分开；轨迹与模型更新两种返回路径。

**需要取舍：** 不继承中心 Logo 的较大视觉占比；训练器可按需要局部展开，而非所有图都保留空框。

<a id="ag06"></a>

## AG06 · AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent (TEA) Protocol

**来源：** [AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent (TEA) Protocol](https://arxiv.org/html/2506.12508v6)；arXiv / 按记录版本。  
**版本／范围：** 2506.12508v6；Fig. 2；PDF 页 []。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 同风格动物头像配角色名；上方主规划器有局部展开，右上是紧凑层级角色图；下方依次放置专用子 Agent、工具、环境和管理组件。

**值得保留：** 统一角色图标家族；角色总览与局部展开；角色—工具的明确归属。

**需要取舍：** 不要搬入整页协议栈和密集图标；只取当前系统有关的局部，角色图标保持相同尺度。

<a id="ag07"></a>

## AG07 · The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents

**来源：** [The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents](https://arxiv.org/pdf/2511.03690v2)；arXiv / 按记录版本。  
**版本／范围：** 2511.03690v2；Fig. 1；PDF 页 [2]。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 左右比较 V0 与 V1；多层组件边界和命名连接表达应用、SDK、workspace、tools 与 server 的依赖及运行边界，主体依然是文字矩形。

**值得保留：** 相同颜色追踪重构前后相对应的模块；边界和依赖关系。

**需要取舍：** 不能作为形体多样性范例；应由我们的词条补充进程、事件、工作区和执行产物等具体对象。

<a id="ag08"></a>

## AG08 · Orchestra-o1: Omnimodal Agent Orchestration

**来源：** [Orchestra-o1: Omnimodal Agent Orchestration](https://arxiv.org/html/2606.13707v1)；arXiv / 按记录版本。  
**版本／范围：** 2606.13707v1；Fig. 2；PDF 页 []。  
**审阅状态：** 已看图面；继承既有记录，本轮未重新核验。

**观察或依据：** 文件图标区分模态，主 Agent 与多个子 Agent 组合，任务依赖与并行执行局部展开；同时存在大面积金属机器人、厚阴影、多种图标及字体处理。

**值得保留：** 按模态呈现输入；主/子 Agent 与任务依赖对照；实际等待关系。

**需要取舍：** 不继承金属机器人、厚阴影和图标风格混杂。不要原样复用价格数字。

<a id="s01"></a>

## S01 · Habitat: A Runtime-Based Computational Performance Predictor for Deep Neural Network Training

**来源：** [Habitat: A Runtime-Based Computational Performance Predictor for Deep Neural Network Training](https://www.usenix.org/system/files/atc21-yu.pdf)；USENIX ATC 2021。  
**版本／范围：** 所链接论文版本／官方页面，查阅日 2026-10-01；图面未核验；PDF 页 []。  
**审阅状态：** 已读技术文本，未核验图面；本轮补充记录。

**观察或依据：** 读到跨 GPU 性能预测、算子测量与硬件条件的技术说明；本轮网页 PDF 截图未取得。

**值得保留：** 硬件条件与预测对象分开、算子到任务预测的语义。

**需要取舍：** 不把 Habitat 描述为 GNN；不从正文推定图形外观。

<a id="s02"></a>

## S02 · Daydream: Accurately Estimating the Efficacy of Optimizations for DNN Training

**来源：** [Daydream: Accurately Estimating the Efficacy of Optimizations for DNN Training](https://arxiv.org/pdf/2006.03318)；USENIX ATC 2020。  
**版本／范围：** 所链接论文版本／官方页面，查阅日 2026-10-01；图面未核验；PDF 页 []。  
**审阅状态：** 已读技术文本，未核验图面；本轮补充记录。

**观察或依据：** 读到低层事件依赖、图变换与模拟执行关系；本轮 PDF 图像读取失败。

**值得保留：** 性能预测应保留计算、通信、等待和依赖；轨迹与关键路径的关系。

**需要取舍：** 不把只读到的文字说明写成已观察的视觉构图；会议为 ATC 2020。

<a id="s03"></a>

## S03 · Heterogeneity-Aware Cluster Scheduling Policies for Deep Learning Workloads (Gavel)

**来源：** [Heterogeneity-Aware Cluster Scheduling Policies for Deep Learning Workloads (Gavel)](https://www.usenix.org/system/files/osdi20-narayanan_deepak.pdf)；OSDI 2020。  
**版本／范围：** 所链接论文版本／官方页面，查阅日 2026-10-01；Fig. 3–4；PDF 页 [5]。  
**审阅状态：** 已看图面；本轮补充记录。

**观察或依据：** 同一作业的时间份额用分段条呈现；任务对的相对吞吐用三角配对矩阵呈现，并区分不可共置条件。

**值得保留：** 时间份额、任务身份与设备类型一致；配对矩阵只展开焦点单元。

**需要取舍：** 时间段不是显存容量；原热图数值和评价配色不迁移成示意实验结果。

<a id="s04"></a>

## S04 · Alpa: Automating Inter- and Intra-Operator Parallelism for Distributed Deep Learning

**来源：** [Alpa: Automating Inter- and Intra-Operator Parallelism for Distributed Deep Learning](https://www.usenix.org/system/files/osdi22-zheng-lianmin.pdf)；OSDI 2022。  
**版本／范围：** 所链接论文版本／官方页面，查阅日 2026-10-01；Fig. 2；PDF 页 [4]。  
**审阅状态：** 已看图面；本轮补充记录。

**观察或依据：** 多种并行方式用重复张量、分块、阶段与时间维度对照。

**值得保留：** 复本与分片的区别；同一个数据片跨设备、阶段保持身份。

**需要取舍：** 只借切分与组织方式；EP/CP 具体通信方案不是此图直接给出的范例。

<a id="s05"></a>

## S05 · HybridFlow: A Flexible and Efficient RLHF Framework

**来源：** [HybridFlow: A Flexible and Efficient RLHF Framework](https://arxiv.org/pdf/2409.19256)；EuroSys 2025。  
**版本／范围：** 所链接论文版本／官方页面，查阅日 2026-10-01；Fig. 1–3；PDF 页 [3, 4]。  
**审阅状态：** 已看图面；本轮补充记录。

**观察或依据：** 圆形角色节点组织 RLHF 数据流；同角色可从逻辑图、放置表对应到设备执行泳道。

**值得保留：** 逻辑角色—放置—执行的对应；不同数据与模型角色分开。

**需要取舍：** 压缩代码块、密集箭头和多层虚线容器；不同 RL 算法不统一成固定四模型图。

<a id="s06"></a>

## S06 · Getting Started with Fully Sharded Data Parallel (FSDP2)

**来源：** [Getting Started with Fully Sharded Data Parallel (FSDP2)](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)；PyTorch 官方教程。  
**版本／范围：** 所链接论文版本／官方页面，查阅日 2026-10-01；仅技术文本；PDF 页 []。  
**审阅状态：** 已读技术文本，未核验图面；本轮补充记录。

**观察或依据：** 官方说明参数、梯度与优化器状态分片，以及聚合、归约、预取和配置相关的重分片。

**值得保留：** 为三状态快照与计算通信泳道提供语义依据。

**需要取舍：** 未审其图面；NVMe 或其他扩展为原创提案，须有实现依据。

<a id="s07"></a>

## S07 · TVM: An Automated End-to-End Optimizing Compiler for Deep Learning

**来源：** [TVM: An Automated End-to-End Optimizing Compiler for Deep Learning](https://www.usenix.org/system/files/osdi18-chen.pdf)；OSDI 2018。  
**版本／范围：** 所链接论文版本／官方页面，查阅日 2026-10-01；Fig. 2–3；PDF 页 [4]。  
**审阅状态：** 已看图面；本轮补充记录。

**观察或依据：** 整体图按图级和算子级分层；局部计算图用不同形状区分输入数据与操作。

**值得保留：** 只借层次分工、数据与操作形态分工，转换后仍保留输入输出身份。

**需要取舍：** 整张文字框层叠和品牌行不作审美模板；代码页与张量切片属于重新构造。

<a id="s08"></a>

## S08 · SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models

**来源：** [SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models](https://arxiv.org/pdf/2211.10438)；ICML 2023。  
**版本／范围：** arXiv v7，2024-03-29；Fig. 2–3；PDF 页 [2, 3]。  
**审阅状态：** 已看图面；本轮补充记录。

**观察或依据：** 激活与权重幅度前后对照；矩阵旁的尺度条区分 tensor、token、channel 级量化。

**值得保留：** 矩阵维度、尺度边条和对应关系；异常通道的局部对照。

**需要取舍：** 不用红绿评价标签替代证据；通用量化不必具备平滑变换。

<a id="s09"></a>

## S09 · vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention

**来源：** [vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention](https://arxiv.org/pdf/2405.04437)；ASPLOS 2025。  
**版本／范围：** 所链接论文版本／官方页面，查阅日 2026-10-01；Fig. 5–6；PDF 页 [6]。  
**审阅状态：** 已看图面；本轮补充记录。

**观察或依据：** 固定虚拟张量与物理页布局的多时刻快照；请求完成后仍保留映射，后来请求可复用。

**值得保留：** 同坐标状态变化；请求身份、映射与物理回收分别表达。

**需要取舍：** 只在有真实回收时清空；前缀树形体另参考 R23，此处不声称展示 radix tree。

**相关依据：** [补充来源1](https://doi.org/10.1145/3669940.3707256)

<a id="s10"></a>

## S10 · DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving

**来源：** [DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving](https://www.usenix.org/system/files/osdi24-zhong-yinmin.pdf)；OSDI 2024。  
**版本／范围：** 所链接论文版本／官方页面，查阅日 2026-10-01；Fig. 6；PDF 页 [9]。  
**审阅状态：** 已看图面；本轮补充记录。

**观察或依据：** Prefill 和 Decode 实例分组，每组内部有模型与执行层；组间显式连接 KV 传输。

**值得保留：** 保留阶段分组、实例边界和中间状态交接。

**需要取舍：** 原图主要是嵌套矩形，取其语义而重画模型层与 KV 薄片；不继承整体方框密度。

<a id="s11"></a>

## S11 · Controllers / Device Plugins / Kubernetes Components

**来源：** [Controllers / Device Plugins / Kubernetes Components](https://kubernetes.io/docs/concepts/architecture/controller/)；Kubernetes 官方文档。  
**版本／范围：** 所链接论文版本／官方页面，查阅日 2026-10-01；仅技术文本；PDF 页 []。  
**审阅状态：** 已读技术文本，未核验图面；本轮补充记录。

**观察或依据：** 协调循环围绕期望与实际状态；设备插件提供设备发现和分配接口；调度绑定与节点启动执行职责分开。

**值得保留：** 控制与执行职责、事件与状态、资源管理与内核提交分开。

**需要取舍：** 工作队列、双状态页等形体为原创提案；插件不放在每次 kernel 提交的必经路径。

**相关依据：** [补充来源1](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)、[补充来源2](https://kubernetes.io/docs/concepts/overview/components/)

<a id="s12"></a>

## S12 · Getting Started with CUDA Graphs

**来源：** [Getting Started with CUDA Graphs](https://developer.nvidia.com/blog/cuda-graphs/)；NVIDIA 作者技术博客，2019。  
**版本／范围：** 所链接论文版本／官方页面，查阅日 2026-10-01；仅技术文本；PDF 页 []。  
**审阅状态：** 已读技术文本，未核验图面；本轮补充记录。

**观察或依据：** 说明捕获、实例化、图提交与减少主机启动开销。

**值得保留：** 同一依赖图的复用，CPU 提交和 GPU 内核保持区分。

**需要取舍：** 重放不是缓存结果，不把原有多个 kernel 画成一个融合算子。


<a id="c01"></a>

## C01 · Kubernetes Components

[官方来源](https://kubernetes.io/docs/concepts/overview/components/)

核验：2026-10-01，仅技术／素材说明文本，未审图面。控制面、节点与实际运行职责。

借鉴：参考组件归属，不把逻辑层次等同物理机位置。 具体构图是原创描述，未生成图片。

<a id="c02"></a>

## C02 · CNCF artwork

[官方来源](https://github.com/cncf/artwork)

核验：2026-10-01，仅技术／素材说明文本，未审图面。官方项目标识的获取入口与素材版本说明。

借鉴：取准确素材；不把素材存在等同已经应用到本库成图。 具体构图是原创描述，未生成图片。

<a id="c03"></a>

## C03 · Persistent Volumes

[官方来源](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

核验：2026-10-01，仅技术／素材说明文本，未审图面。PV、PVC、卷后端及生命周期等技术语义。

借鉴：区分管理声明与实际数据读写，避免串行控制器读写路径。 具体构图是原创描述，未生成图片。

<a id="c04"></a>

## C04 · Kubernetes Icons Set

[官方来源](https://github.com/kubernetes/community/blob/main/icons/README.md)

核验：2026-10-01，仅技术／素材说明文本，未审图面。Kubernetes 资源图标集合及使用入口。

借鉴：可采用资源身份图标；不要求整图全部套用图标外形。 具体构图是原创描述，未生成图片。

<a id="c05"></a>

## C05 · Kubernetes Service

[官方来源](https://kubernetes.io/docs/concepts/services-networking/service/)

核验：2026-10-01，仅技术／素材说明文本，未审图面。逻辑服务与后端端点的抽象关系。

借鉴：服务图标不是新增物理交换机，逻辑调用与网络连通分层。 具体构图是原创描述，未生成图片。


## 综合绘图方法与配色来源（2026-10-02）

以下来源的具体取舍已写入本技能入口、视觉规范与构图规则，不是独立技能依赖：

- [Vivid Figures](vivid-figures-ideas.md)：表达形式选择、视觉基线与有共同参照的叠加。
- [figures4papers](figures4papers-ideas.md)：已看三幅实际图；多色对象身份、同族变体、主图与局部展开。
- [Framework Studio](framework-studio-ideas.md)：已看两幅实际图；真实关系与画面分组分开核对、操作位置和连线语义。

来源审阅范围和版本见各记录；新增配色组合是候选，需要在实际成图中判断，未标为用户验收。
