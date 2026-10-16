# Diátaxis 简体中文翻译规范

本文件是 `translation/zh_CN/LC_MESSAGES/*.po` 的翻译与校订依据。所有改动都必须先满足本规范。

---

## 0. 总则：上游作者的授权

上游 `source/translation.rst` 中作者对译者的要求，就是本项目的最高准则：

> I prefer translations to contain good translations for key terms **in their own language**.
> Even if it's common to use the English term "how-to" in your language, I don't want the
> translations to do that. They should find a native alternative, and use it consistently.
>
> I care much more about **the meaning and force of the ideas** in Diátaxis than the
> preservation of the way I have expressed them in English. I certainly don't want or expect
> literal translation. Translations should be idiomatic and sound unforced. Use native
> sentence structures and constructions. If better metaphors or turns of phrase exist in your
> language, use those.

因此本项目的取向明确：**不逐字直译，重意与势，追求地道自然。** 这正对应「信达雅」：

| 层次 | 要求 | 反面 |
|---|---|---|
| **信** | 意思、语气、逻辑关系、强调点与原文一致；不增、不减、不改写论点 | 添油加醋、漏译限定语、把陈述改成建议 |
| **达** | 中文通顺，符合汉语表达习惯，读来不觉得是译文 | 翻译腔、欧化长句、代词滥用、被动泛滥 |
| **雅** | 节奏与气韵贴合原文：该凝练处凝练，该绵长处绵长，保留原文的比喻与机锋 | 平铺直叙、把警句译成说明书 |

> 三条冲突时，优先级为 **信 > 达 > 雅**。但「信」指忠于**意思与语气**，不指忠于**英文语序与词形**。

---

## 1. 术语表（强制统一）

### 1.1 四类文档

| English | 中文（唯一写法） | 说明 |
|---|---|---|
| Tutorials | **教程** | 不加「文档」「类」等后缀 |
| How-to guides | **实践指南** | 不用「操作指南」「如何做指南」「how-to」 |
| Reference | **参考资料** | 指文档类型时用此；`reference guide` 可作「参考指南」 |
| Explanation | **解释说明** | 指文档类型时用此 |

四者并列时保持同一层级、同一词形，不混用「教程文档／实践指南／参考／解释」。

### 1.2 两个维度、四个取向 —— **中文版的核心本地化设计，不得拆改**

> ⚠️ **这是本项目的既定设计，不是可选项。**
> 中文版用「**知与行**」「**学与用**」两组对偶来概括 Diátaxis 的两个维度：
> 知＝认知与理解，行＝行动与实践；学＝习得知识与技能，用＝运用知识与技能。
> 它们区分**文档所支持的活动**与**用户当前的目的**，不表示用户水平，也不是固定的先后阶段。
> 这一设计已写入 `README.rst`，并且**已经固化在 `source/images/zh_CN/*.svg` 全部中文图示中**。
> 文字与图示用词必须完全一致，否则站点自相矛盾。

| English | 单字 | 完整形式 | 一般行文用词 |
|---|---|---|---|
| action | **行** | **行（行动）** | 行动 |
| cognition | **知** | **知（认知）** | 认知 |
| acquisition | **学** | **学（习得）** | 习得 |
| application | **用** | **用（应用）** | 应用 |
| study | **学** | **学** | 学习 |
| work | **用** | **用** | 工作 |
| learning-oriented | — | — | 面向学习 |
| goal-oriented / task-oriented | — | — | 面向目标／面向任务 |
| information-oriented | — | — | 面向信息 |
| understanding-oriented | — | — | 面向理解 |

**强制规则：**

> **核心判据：这个词在句子里是「独立术语」，还是「句子的一个成分」？**
>
> 汉语里「行、知、学、用」四个单字可以当**标签**用（`知与行`、`学与用`、表格里的坐标轴名），
> 但当**词**用就很别扭——「指导行」「用户的学」都不像话。所以注解的位置要分两种情况：

| 情形 | 写法 | 例 |
|---|---|---|
| **独立术语**：英文用粗体／斜体单独标出的框架词、坐标轴标题、表格里的坐标轴单元格、定义句中被点名的术语 | **单字在前**：`X（Y）` | `**行（行动）**`、`*学（习得）*`、`知与行`、`*行（行动）还是知（认知）？*` |
| **句中成分**：该词作主语、宾语、定语、状语，或与动词构成动宾短语，已融入句子 | **自然词在前**，需要注解时缀在其后：`Y（X）` | `指导行动（行）`、`服务于技能的应用（用）`、`*运用（用）*知识` |

1. **英文把该词标为框架术语时**（原文写成 `**action**`、`**cognition**`、`**study**`、
   `**work**`、`**acquired**`、`**applied**` 等粗体），中文**必须**保留**相同的标记种类与数量**，
   并按上表选定形式。不得改写成 `**行动**`、`**认知**` 而丢掉单字与注解，
   也不得写成 `指导行（行动）` 这类把单字硬塞进动宾短语的形态。
2. **坐标轴标题**：`Action/cognition` → **`知与行`**；`Acquisition/application` → **`学与用`**。
   与图示一致，不得改成「行动/认知」「习得/应用」。
3. **一般行文**（英文未标粗、非坐标轴语境）用自然词：行动、认知、习得、应用、学习、工作，
   不加粗、不加注解。
4. **能不加注解就不加**。注解只用来建立一次对应关系；
   **同一段落内已注解过一次的，后文不再重复**。
5. **绝不为了加注解而添加原文没有的句子、从句或分句。**
   **唯一经批准的例外**（已确认保留，不要当作错误改掉）：`foundations.rst` 的小节标题
   `Two dimensions of craft` 作「技艺的两个维度：知与行、学与用」——这是全书首次引入两个维度之处，
   与 README 的表述一致，加这一笔是为了让读者在此处就拿到「知/行/学/用」这套坐标。**除此之外不得增补。**
6. 涉及坐标系、四象限、指南针表格（`compass.rst`、`start-here.rst` 的指南针表、
   `map.rst` 的模糊表、`foundations.rst` 的需求表）时，按上表分别处理：
   单元格若是**名词性术语**用单字在前，若是**动宾短语或偏正短语**则自然词在前。
   用词须与 `source/images/zh_CN/diataxis.svg`、`axes-of-needs.svg` 保持一致。

**参照图示的既有措辞（不得出现矛盾说法）：**

* `diataxis.svg`：「Diátaxis 的两个维度是知与行、学与用。纵向上方为行（行动），下方为知（认知）；
  横向左侧为学（习得），右侧为用（应用）。」
* `overview-how-to.svg`：「行与用：实践指南帮助读者通过行动完成实际目标。」
* `overview-reference.svg`：「知与用：参考资料提供读者在工作中查用的知识信息。」
* `overview-explanation.svg`：「知与学：解释说明帮助读者建立认知、加深理解。」
* `overview-tutorials.svg`：「行与学：教程帮助读者通过行动习得知识与技能。」

### 1.3 其他关键术语

| English | 中文 | 备注 |
|---|---|---|
| craft | 技艺 | 贯穿全书的中心词 |
| practitioner | 实践者 | 不用「从业者」「练习者」 |
| discipline | 学科；专业领域 | **绝不译作「纪律」**（`maintain the discipline of writing` 是「保持写作的严谨」） |
| machinery | 系统 | 指被文档描述的对象，全站统一用「系统」。`the product and its internal machinery` 作「产品及其内部构造」。不用「机制／设备／机器」 |
| flow | 流畅感；心流 | `having flow` → 「流畅感」；`gives the user flow` → 「让用户进入流畅状态」 |
| feeling of doing | 行事的感受 | 全书统一 |
| encounter | 相遇 | **已确认保留的术语**，3 处（`start-here`、`tutorials-how-to` ×2）。作者用它指「学习者与工具、概念之间被安排好的照面」，属刻意选词。虽有「接触」等更平实的说法，仍统一作「相遇」，不要改 |
| reflection | 反思 | 动词 `reflect` → 「反思」 |
| heuristic | 启发式（方法） | |
| propositional knowledge | 命题性知识 | 与「理论性知识」互文 |
| deep quality | 深层品质 | `quality.rst` 核心对偶 |
| functional quality | 功能品质 | 同上 |
| austere | 严谨克制 | 形容参考资料风格 |
| contrived setting | 人为搭建的场景 | `tutorials-how-to` |
| cycle of interaction | 交互循环 | `map.rst`、`tutorials-how-to.rst` |
| course-correction tool | 校正方向的工具 | |
| banal | 平淡无奇 | 「surprisingly banal」→「出人意料地平淡无奇」 |
| compass / map | 指南针／地图 | 始终保留比喻，不改成「工具／结构」 |
| user needs | 用户需求 | |
| at study / at work | 处于「学」的状态／处于「用」的状态 | 需要点时写作 `**学**` / `**用**` |
| learner / student / pupil | 学习者／学生／学生 | 保留原文的用词变化，不一律抹平为「用户」 |
| tutor / teacher / instructor | 导师／教师／讲师 | 同上，随原文 |
| rubric | （不译） | Sphinx 结构，见 §3 |

---

## 2. 语气与文风

1. **保留原文的断言力度。** 原文是祈使句就译祈使句，原文斩钉截铁就不要译成「建议……」。
   - ✅ `Don't do that. It's horrible.` → 「别这么做，那很糟糕。」
   - ❌ 「建议不要这样做，效果可能不理想。」
2. **保留第一人称与第二人称。** 原文用 `I`（作者自述）、`you`（对读者说话）、`we`（师生共同体）时，
   中文照译「我／你／我们」，不要改成无人称的客观陈述。
3. **少用被动。** 英文被动语态在中文里优先转成主动或无主句。
   - ❌ 「这些区别被允许模糊时」 → ✅ 「一旦任由这些区别模糊下去」
4. **去掉冗余代词与连接词。** 中文不需要每句都补「它」「这」「因此」「而且」。
5. **长句要断。** 英文的复合长句在中文里常常需要拆成两三个短句，用分号或句号断开，而不是靠「以及」「并且」硬连。
6. **保留原文的排比与重复。** 作者常刻意重复同一句式（如 `X is not Y. It is Z.`），
   中文也应保持同等重复，不要为了「变化」而改写。
7. **标题译法。** 英文标题多为名词短语或祈使句。中文标题求短、求准，不加句号。
   - `Seek flow` → 「追求流畅感」；`Just do something` → 「动手做点什么」
   - `Do what you like` → 「随你所用」（不是「做你喜欢的事」——这里是「你可以随意使用」之意）
8. **比喻要留住。** `the instructor is condemned to be absent`（讲师注定缺席）、
   `a cradle for this feeling`（孕育这份感受的摇篮）、`bleed into each other`（彼此渗透）
   这类比喻是原文的力量所在，必须用中文的比喻接住，不能改成平白说明。
9. **框架术语按 §1.2 处理。** 「知／行／学／用」是中文版的核心设计，与中文图示绑定。
   见到 `**action**`、`**cognition**`、`**study**`、`**work**` 这类粗体框架词，
   必须扩写为 `**行（行动）**`、`**知（认知）**`、`**学（习得）**`、`**用（应用）**`，
   **不要**图省事压成 `**行动**`、`**认知**`——那会让正文与图示对不上。

---

## 3. 标记与结构：不得改动

`.po` 的 `msgstr` 中，下列内容必须与 `msgid` **完全一致**，一个字都不能变：

1. **Sphinx 角色目标**：`:doc:`、`:ref:`、`:class:`、`:meth:` 等角色中的 `` `<target>` `` 部分。
   - `:doc:`systematic theoretical principles <theory>`` → `:doc:`系统的理论原则 <theory>``  ✅ 目标 `theory` 未变
   - ❌ `:doc:`系统的理论原则 <理论>``
2. **字面量**：所有 ` ``...`` ` 内的内容原样保留（代码、文件名、字符串示例）。
3. **链接**：`` `text <https://...>`_ `` 中的 URL 原样保留，链接文字可译。
4. **`\\\\` 等转义**、`msgid` 里的换行结构、以及 `sphinx.po` 中的 `%` 占位符。
5. **不翻译**：`Diátaxis`、`Sphinx`、`Transifex`、`GitHub`、`Read the Docs`、人名、书名、
   `#diataxis` 频道名、`CITATION.cff`、`atom.xml`、产品名、代码标识符。

---

## 4. 强调标记：与英文一一对应

**这是最容易出错的地方，逐条核对。**

| 英文 | 中文 | 规则 |
|---|---|---|
| `**粗体**` | `**粗体**` | 保持粗体 |
| `*斜体*` | `*斜体*` | 保持斜体 |

* **不得增删**：英文没有加粗的句子，中文不得加粗；英文加粗的，中文必须加粗。
* **不得升降级**：`*x*` 不能译成 `**x**`，`**x**` 不能译成 `*x*`。
* **章节标题**按原文处理；原文标题不加粗，中文标题也不加粗。
* 英文对**单个词**的强调，在中文里如果该词无法单独成立，可以强调**最小的自然短语**，
  但必须保持同一标记种类。例如 `*Later*` → `*稍后*`（不是 `**稍后**`）。
* 强调一段完整的话时，`*...*` 或 `**...**` 应包住中文的完整意群，标记内**不留首尾空格**。

---

## 5. 标点与排版

> ### ⚠️ 先读这一条：为什么中文可以紧贴标记
>
> docutils 默认的行内标记规则要求：标记的**开头**必须紧跟在空白或标点之后，
> **结尾**之后也必须是空白或标点。汉字属于 Unicode 字母类，两条都不满足，
> 因此默认情况下 `中文**粗体**中文` **不会**被解析成粗体，而是原样显示一对星号——
> 句法校验看不出来，只有真正渲染一遍才会暴露。
>
> 本项目通过 `source/docutils.conf` 开启了 docutils 的
> `character-level-inline-markup`，取消了这一位置限制。
> 于是 `中文**粗体**中文` 能正确解析，**中文正文无需为迁就解析规则插入多余空格**。
> 该设置对英文站点无任何影响（英文构建产物逐字节相同）。
>
> **改动 `docutils.conf` 或调整构建方式时，务必重跑 `tools/check-render.py` 验证。**

1. **破折号。** 英文用 ` - `（前后带空格的连字符）充当破折号时，中文一律用全角破折号 `——`，
   前后不加空格。若破折号出现在行末换行处，注意 `——` 不可拆开显示为两个 `—`。
   - `Start here - Diátaxis in five minutes` → 「从这里开始——五分钟了解 Diátaxis」
   - `- facts -` → 「——即事实——」
2. **标记与中文之间不加空格。**
   - ❌ `四种类型是： **教程**， **实践指南** 和 **解释说明** 。`
   - ✅ `四种类型是：**教程**、**实践指南**、**参考资料**和**解释说明**。`
   - ❌ `对于它 *为什么* 起作用` → ✅ `对于它*为什么*起作用`
3. **但拉丁字母／数字与中文之间要保留一个半角空格**，标记也不例外：
   - ✅ `Diátaxis *为什么*有效`（`Diátaxis` 与 `为什么` 分属拉丁与中文，空格正确）
   - ✅ `请参阅 :doc:`Sphinx 文档 <sphinx>``
   - 判据：空格两侧若**都是中文**，则空格是多余的；若一侧是拉丁字母或数字，则空格应当保留。
4. **超链接标记同理**：`**参考资料包含技术描述**——即……`（`——` 紧贴，不留空格）。
5. **中文与拉丁字母／数字之间加一个半角空格**：`使用 Python 创建`、`第 3 步`、`Diátaxis 地图`。
6. **中文标点用全角**：`，。；：？！（）「」` 或 `“”`。不得出现 ` 。`、` ，`、` ）` 这类
   「半角空格＋全角标点」的组合。
7. **表示并列的顿号用 `、`**，不用 `，`：
   - ❌ `准确，完整，可靠` → ✅ `准确、完整、可靠`
8. **省略号用 `……`**（两个，共六点），不用 `...` 或 `。。。`。
9. **引号统一用中文 `“”`**，引号内是英文词时可用 `“flow”`。书名、术语首次出现可用 `*斜体*`
   随原文，或直接用中文书名号《》对应英文书名。
10. **英文圆括号→中文全角 `（）`**，但括号内全是英文时保留半角并用空格隔开：
    `HTTP（Hypertext Transfer Protocol）`。
11. **全角标点前后不留空格**：`……（*我该如何制作……？*）`，不写 `** （` 或 `） 。`。
12. `%`、`&`、`#` 等符号在 `sphinx.po` 中按原样保留。

---

## 6. 常见病症与改法

| # | 病症 | 反例 | 改法 |
|---|---|---|---|
| 1 | **译文腔长定语** | 「它服务于人们理解事物、并将其置于更宏大图景之中的需要」 | 「它的用处，是帮人理解事物，把事物放进更大的图景里」 |
| 2 | **滥用「进行」「加以」「予以」** | 「对文档进行改进」 | 「改进文档」 |
| 3 | **「的」字堆叠** | 「这是文档的问题的核心的症结」 | 「这正是文档问题的核心症结」 |
| 4 | **机械对应 `and`** | 「准确和完整和可靠」 | 「准确、完整、可靠」 |
| 5 | **该断句不断** | 一句话套三个从句 | 拆成短句，用句号或分号 |
| 6 | **丢失限定词** | `partly because...` 只译「因为」 | 「部分原因是……」「一半是因为……」 |
| 7 | **改写论点** | 原文说 A 不好，译文说「A 可能不太理想」 | 恢复原文力度 |
| 8 | **增补原文没有的内容** | 凭空加一句解释、补一段背景 | **删掉**。忠实优先（§1.2 规则 5 批准的例外除外） |
| 9 | **术语漂移** | 同一篇里 reference 时而「参考」时而「参考资料」 | 按 §1 统一 |
| 10 | **比喻落地** | `condemned to be absent` → 「不能在场」 | 「注定缺席」 |

---

## 7. 作业流程（修订 `.po` 时必须遵守）

**不要手工编辑 `.po` 文件的语法。** 一律通过下面的三步流程改写，以保证 PO 结构与折行不被破坏：

```bash
# 1. 通读原文（英文 source）与现有译文
#    source/<name>.rst          英文原文
#    .venv/bin/python tools/dump-pairs.py <name>     中英对照
.venv/bin/python tools/dump-pairs.py tutorials

# 2. 把「msgid -> 新 msgstr」写成 JSON（键必须是 msgid 原文，逐字一致）
cat > /tmp/tutorials-new.json <<'JSON'
{
  "Show the learner where they'll be going": "让学习者知道此行的去向",
  "...": "..."
}
JSON

# 3. 套用并校验（反复迭代直到 0 error）
.venv/bin/python tools/apply-translations.py translation/zh_CN/LC_MESSAGES/tutorials.po /tmp/tutorials-new.json
.venv/bin/python tools/check-po.py translation/zh_CN/LC_MESSAGES/tutorials.po
```

`apply-translations.py` 只会替换 `msgstr` 块，文件头、注释、`msgid`、顺序、flags 全部逐字节保留。

## 8. 交付前的自检清单

改完一个 `.po` 文件后，逐条确认：

- [ ] `.venv/bin/python tools/check-po.py translation/zh_CN/LC_MESSAGES/<file>.po` **0 error**
- [ ] `.venv/bin/python tools/check-render.py <file>` **0 error**（标记真的会被解析，不会原样显示星号）
- [ ] `.venv/bin/python tools/check-terms.py <file>` 无「知/行/学/用 框架术语」问题
- [ ] 所有 `:role:` 的目标字符串、所有 ` ``literal`` `、所有 URL 与英文一致
- [ ] `*` 与 `**` 的数量、种类与英文**逐一对应**，没有增删或升降级
- [ ] 全文没有残留的 ` - `（英文式破折号）
- [ ] 行内标记与中文之间没有多余空格；没有 ` 。`、` ，`、` （` 这类组合
- [ ] 术语符合 §1；同一术语全文写法唯一
- [ ] 没有添加原文没有的信息；没有漏掉原文的限定语、否定、反讽
- [ ] 中文读起来不像译文：默读一遍，拗口处重写
- [ ] 保留了原文的比喻、排比、重复与语气强度

## 9. 参考译例（可作为语气基准）

| 原文 | 首选译文 | 说明 |
|---|---|---|
| Treat this website as a handbook or a toolbox that you make use of when you need it. | 把本网站当作一本手册、一只工具箱，需要时取用。 | 短句、对举，去掉「在你需要时使用」的译文腔 |
| The best way to get started with Diátaxis is by applying it - to something, however small. | 入门 Diátaxis 的最好办法，就是把它用起来——用在什么东西上都行，多小都行。 | 保留原文破折号后的追加语气 |
| A tutorial is a lesson, that takes a student by the hand through a learning experience. | 教程是一堂课，牵着学生的手，带他走完一段学习经历。 | 「牵着……的手」是原文比喻，不能丢 |
| The instructor is condemned to be absent. | 讲师注定缺席。 | 保留「注定」的宿命感 |
| Explanation brings clarity, light and context. | 解释说明带来清晰、光亮与背景。 | 保留原文的三词排比 |
| Good documentation **feels good**. | 好的文档**手感是好的**。 | 保留粗体与口语力度 |
| It's surprisingly banal. | 它出人意料地平淡无奇。 | 不改成「非常简单」 |
| Don't do that. It's horrible. | 别这么做，那很糟糕。 | 祈使句＋短促判断 |
