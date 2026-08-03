from __future__ import annotations

import re
from pathlib import Path


def _norm_q(s: str) -> str:
    s = s.replace("？", "?")
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = re.sub(r"\s+", " ", s).strip()
    return s


TRANSLATIONS: dict[str, str] = {
    _norm_q("Living in the countryside or having an urban life, which one do you prefer?"): "住在乡村还是过城市生活，你更喜欢哪一个？",
    _norm_q("Please use examples or your personal experience to support your opinion."): "请用例子或个人经历来支持你的观点。",
    _norm_q(
        "The mass media (mass communication) including TV, Radio and newspaper influence our society and shape our opinions and characters. What is your opinion?"
    ): "包括电视、广播、报纸在内的大众媒体会影响社会并塑造我们的观点和性格。你怎么看？",
    _norm_q(
        "Information revolution has changed the way of mass communications and had some negative and positive effects on individual lives as well as on society. To what extent do you agree or disagree?"
    ): "信息革命改变了大众传播方式，并对个人生活和社会产生了正反两方面影响。你在多大程度上同意或不同意？",
    _norm_q("Whether mass media including TV, Radio and newspaper will influence our society and shape our opinions and characters？"): "包括电视、广播、报纸在内的大众媒体是否会影响社会并塑造我们的观点与性格？",
    _norm_q(
        "Nowadays the way people communicate with each other has changed in society. Discuss its positive and negative effects. Whether the new method of communication has more positive effects."
    ): "如今人们的沟通方式发生了变化。讨论其积极和消极影响，并说明这种新沟通方式是否积极影响更多。",
    _norm_q(
        "Should marketing for consumer goods companies like clothing and food focus on reputation or on short term strategies like discount and special offers? Why?"
    ): "服装、食品等消费品公司的营销应注重声誉，还是应注重折扣/特价等短期策略？为什么？",
    _norm_q("Whether studying films at school is as important as studying literature?"): "在学校学习电影是否和学习文学一样重要？",
    _norm_q("Do you think school should have curriculum asking students to play old drama and work for theatre centuries ago?"): "你认为学校是否应该设置课程，让学生演出数百年前的旧戏剧作品？",
    _norm_q(
        "There are both problems and benefits for high school students study plays and works of theatres written centuries ago. Discuss and use your own experience"
    ): "高中生学习几百年前写的戏剧作品既有好处也有问题。请讨论并结合你的经历。",
    _norm_q(
        "Some famous people such as pop-stars and sportsman give up the right to privacy, because this is the price of fame. To what extent do you agree/disagree with this point of view? Give your opinion with your experiences."
    ): "有人认为流行歌手、运动员等名人必须放弃隐私权，因为这是成名的代价。你在多大程度上同意或不同意？请结合经历说明。",
    _norm_q(
        "In modern society, unemployment among young people is a serious problem. One solution is to shorten the working week. Give your opinion of the idea, considering the advantages and disadvantages, whether it can apply to young people or the whole workforce."
    ): "在现代社会，青年失业是严重问题。一种解决办法是缩短工作周。请评价这一想法，考虑其利弊，并说明它适用于年轻人还是整个劳动力群体。",
    _norm_q(
        "\"In the future, people will work less hours at their jobs.\" To what extent do you agree with it? Please support your opinion with your own experience"
    ): "“未来人们在工作中会减少工时。”你在多大程度上同意？请用你的经历支持观点。",
    _norm_q("It is important to preserve beautiful buildings from the past, even it is expensive for owner to do so. Agree or Disagree?"): "即使维护成本很高，也应当保护过去的精美建筑。你同意还是不同意？",
    _norm_q("Governments spend much money on preserving beautiful old buildings rather than building modern buildings. Agree or Disagree?"): "政府应该把大量资金用于保护漂亮的旧建筑，而不是建现代建筑。你同意还是不同意？",
    _norm_q(
        "More and more countries spend large amounts of money on the restoration of buildings instead of on modern housing. To what extent do you agree or disagree with this analysis? Support your writing with your experience and/or examples."
    ): "越来越多国家把大量资金用于修复建筑，而不是用于现代住房建设。你在多大程度上同意或不同意？请用经历或例子支持。",
    _norm_q("Should we have a maximum wage for the high-paid jobs?"): "是否应该为高薪工作设定最高工资上限？",
    _norm_q("In some companies, employers take workers' opinions into consideration of products and services. Discuss the advantages and disadvantages."): "在一些公司里，雇主在产品和服务方面会考虑员工意见。讨论其优缺点。",
    _norm_q("Company’s top-level authorities should involve their employees in decision-making process. Discuss the advantages and disadvantages."): "公司高层应让员工参与决策过程。讨论其优缺点。",
    _norm_q(
        "Nowadays TV has become an essential part of life. It is a medium to spread news & awareness and for some it acts like a companion. What is your opinion about this?"
    ): "如今电视已成为生活必需品。它传播新闻与信息，有些人还把它当作陪伴。你怎么看？",
    _norm_q(
        "How widely of you think the problem spreads that people spend too much time on work than their personal life and experience time shortage? What problems will it cause?"
    ): "你认为人们工作时间过多、个人生活时间不足（时间短缺）的问题有多普遍？会造成哪些问题？",
    _norm_q(
        "类似题目1：It is important to maintain the balance between work and other aspect of person’s life such as family and leisure time, agree or disagree? Why it is hard to achieve?"
    ): "类似题目1：保持工作与生活其他方面（如家庭与休闲）的平衡很重要。你同意还是不同意？为什么很难做到？",
    _norm_q(
        "In the past 100 years, there are many inventions such as antibiotics, airplanes and computer. What do you think is the most important invention for the past 100 years? Why?"
    ): "过去100年出现了许多发明，如抗生素、飞机、计算机。你认为过去100年最重要的发明是什么？为什么？",
    _norm_q(
        "Some people believe that human behavior can be changed by laws; others argue that laws have little effect on human behaviour. Which opinion do you agree with? Please explain."
    ): "有人认为法律可以改变人类行为；也有人认为法律对行为影响很小。你同意哪种观点？请解释。",
    _norm_q("In developing countries, tourism has disadvantages and advantages."): "在发展中国家，旅游业既有优点也有缺点。",
    _norm_q("【变体 1】Discuss the advantages and disadvantages of tourism in less developed countries."): "【变体1】讨论欠发达国家旅游业的优点和缺点。",
    _norm_q("【变体 2】The negative impacts of tourism in less developed countries: challenges and sustainable solutions"): "【变体2】欠发达国家旅游业的负面影响：挑战与可持续解决方案。",
    _norm_q("The advanced medical technology expands human’s life. Do you think it is a curse or blessing?"): "先进医疗技术延长了人类寿命。你认为这是福还是祸？",
    _norm_q("It is getting harder for children to live and grow in the 21st century than in the past. Do you agree or disagree?"): "与过去相比，21世纪孩子的生活与成长更难。你同意还是不同意？",
    _norm_q("Travel to study is over rated, we have brilliant scholars who studied locally. Is travel really required for higher studies?"): "为了学习而旅行/异地求学被高估了，因为也有许多在本地学习的杰出学者。高等教育真的需要旅行/异地学习吗？",
    _norm_q("【变体1】Travel is necessary or not necessary for a quality education."): "【变体1】旅行对优质教育是否必要？",
    _norm_q("【变体2】Is traveling necessary for a good education? Some smart scholars never leave their hometowns."): "【变体2】旅行对良好教育是否必要？一些聪明的学者从未离开过家乡。",
    _norm_q("Should schools make learning a foreign language compulsory?"): "学校是否应把外语学习设为必修？",
    _norm_q("Government should create a better network of public transport available for everyone or build more roa ds owning population？"): "政府应该建立更完善、人人可用的公共交通网络，还是为拥有私家车的人修更多道路？",
    _norm_q("What are the advantages of cheaper public transportation? What will it cause to achieve it?"): "更便宜的公共交通有哪些优势？为了实现这一点会带来什么影响/代价？",
    _norm_q("The formal written examination can be a valid method to assess students' learning. To what extent do you agree or disagree?"): "正式笔试可以作为评估学生学习情况的有效方式。你在多大程度上同意或不同意？",
    _norm_q(
        "Do you agree that education system that assesses the student's learning by written exam is correct?Please discuss the significance of formal written assessments in today's world to evaluate children's performance"
    ): "你是否同意用笔试评估学生学习的教育体系是正确的？请讨论在当今世界，正式笔试在评估学生表现方面的重要性。",
    _norm_q(
        "Age restrictions can be seen everywhere. It is believed that people should not do things until they reach the right age, such as marriage, and driving. Select one activity and state the minimum age that you think."
    ): "到处都有年龄限制。人们认为只有达到合适的年龄才能做某些事情，如结婚、开车。请选择一项活动，并说明你认为的最低年龄。",
    _norm_q("Support with your own experiences."): "请用你自己的经历进行支持/举例。",
    _norm_q("Is it fair for universities to deduct students’ marks when their assignments are overdue? How to solve this problem?"): "大学在作业逾期时扣学生分是否公平？如何解决这一问题？",
    _norm_q("Large shopping malls are replacing small shops. What is your opinion about this? Discuss with appropriate examples."): "大型购物中心正在取代小商店。你怎么看？请结合恰当例子讨论。",
    _norm_q("Write about Climate change? Who is responsible whether Government or industries? Why?"): "谈谈气候变化：政府还是企业/工业应承担责任？为什么？",
    _norm_q("Experience is more effective and useful than books and formal education. What is your opinion?"): "经验比书本和正规教育更有效、更有用。你怎么看？",
    _norm_q(
        "Some people think that life experience is more important than the formal education provided in schools and universities. How far do you agree with this statement, and provide examples?"
    ): "有人认为生活经验比学校和大学提供的正规教育更重要。你在多大程度上同意？并请举例。",
    _norm_q("Whether experiential learning (learning by doing) can work well in formal education. Do you agree or disagree?"): "体验式学习（做中学）是否能在正规教育中有效？你同意还是不同意？",
    _norm_q(
        "Study needs time, peace and comfort, whereas employment needs the same thing. Someone says it is impossible to combine those two because one distracts one another. Do you think this is realistic in our life today? To what extent do you agree with it? Support your opinion with example."
    ): "学习需要时间、安静与舒适，而工作也需要这些。有人说两者无法兼顾，因为会互相干扰。你认为在当今生活中这是否现实？你在多大程度上同意？请举例支持。",
    _norm_q("Technology has made the world a better place to live. To what extent do you agree with this statement?"): "科技让世界变得更适合居住。你在多大程度上同意？",
    _norm_q("Design of buildings have positive or negative impact on people’s life and work?"): "建筑设计会对人们的生活和工作产生积极还是消极影响？",
    _norm_q("Parents should be held legally responsible for children’s acts. What is your opinion? Support it with personal examples."): "父母应当对孩子的行为承担法律责任。你怎么看？请用个人例子支持。",
    _norm_q("Which one is better, Textbook library or new digital material in university."): "大学里教材/实体图书馆与新的数字资料，哪一种更好？",
    _norm_q("With the increase of digital media available online, the role of the library has become obsolete."): "随着在线数字媒体的增多，图书馆的作用已经过时/变得无足轻重。",
    _norm_q("Universities should only procure digital materials rather than constantly textbooks."): "大学应只采购数字资料，而不是不断采购纸质教材。",
    _norm_q("Discuss both the advantages and disadvantages of this position and give your own point of view."): "讨论这一观点的优缺点，并给出你自己的看法。",
    _norm_q(
        "When people need to complain about a product or a service, some prefer to complain in writing while others prefer to complain in person. Which way do you prefer?"
    ): "当人们要投诉产品或服务时，有些人喜欢书面投诉，有些人喜欢当面投诉。你更偏好哪种方式？",
    _norm_q("Governments and international institution are faced with many global problems."): "政府和国际机构面临许多全球性问题。",
    _norm_q("What these problems could be? What solution would you suggest?"): "这些问题可能是什么？你会建议哪些解决方案？",
    _norm_q("The pressing problem: The world’s governments and organizations confront a multigrade of issues."): "紧迫问题：世界各国政府和组织面临多种问题。",
    _norm_q("What is the most pressing problem facing the inhabitants of our planets and what are the solutions?"): "地球居民面临的最紧迫问题是什么？解决方案有哪些？",
    _norm_q("You need to study climate change."): "你需要研究气候变化。",
    _norm_q("Which aspect of climate change will you choose and why?"): "你会选择研究气候变化的哪个方面？为什么？",
    _norm_q("You are given climate change as the field of study."): "你的研究领域被指定为气候变化。",
    _norm_q("Which area would you prefer?"): "你更偏好研究哪个领域/方向？",
    _norm_q("Explain why you pick this particular area of your study and give an example in the area you pick"): "解释你为何选择这个研究方向，并给出该领域的一个例子。",
}


def _split_sections(text: str) -> list[tuple[int, list[str]]]:
    lines = text.splitlines()
    sections: list[tuple[int, list[str]]] = []
    num: int | None = None
    buf: list[str] = []

    for line in lines:
        stripped = line.strip()
        m = re.match(r"^(\d+)\.$", stripped)
        m_report = re.match(r"^--(\d+)\.\[.*\]$", stripped)
        if m or m_report:
            if num is not None:
                sections.append((num, buf))
            num = int((m or m_report).group(1))
            buf = []
            continue
        if num is not None:
            buf.append(line)

    if num is not None:
        sections.append((num, buf))

    return sections


def _first_english_bracket(text_line: str) -> str | None:
    for content in re.findall(r"\[(.*?)\]", text_line):
        if re.search(r"[A-Za-z]", content):
            return content.strip()
    return None


def _find_next_english_bracket(lines: list[str], idx: int, lookahead: int = 10) -> str | None:
    for j in range(idx, min(idx + lookahead, len(lines))):
        c = _first_english_bracket(lines[j])
        if c:
            return c
    return None


def _extract_stance(lines: list[str]) -> str | None:
    for i, line in enumerate(lines):
        if "I tend to be" in line:
            c = _find_next_english_bracket(lines, i, lookahead=6)
            if c:
                return c

    for i, line in enumerate(lines):
        m = re.search(r"From my perspective,\s*I\s+(agree|disagree)\b.*?that", line, re.IGNORECASE)
        if m:
            verb = m.group(1).lower()
            c = _find_next_english_bracket(lines, i, lookahead=6)
            if c:
                return f"I {verb} that {c}"

    for i, line in enumerate(lines):
        if "From my perspective" in line:
            c = _find_next_english_bracket(lines, i, lookahead=6)
            if c:
                return c

    for line in lines:
        m = re.search(r"\bchoose to\s+(.*?)(?:\.|$)", line, re.IGNORECASE)
        if m:
            return m.group(1).strip()

    for line in lines:
        m = re.search(r"\bis that\s+(.*?)(?:\.|$)", line, re.IGNORECASE)
        if m:
            return m.group(1).strip()

    return None


def _extract_reason(lines: list[str], needle: str) -> str | None:
    for i, line in enumerate(lines):
        if needle in line:
            c = _find_next_english_bracket(lines, i, lookahead=8)
            if c:
                return c
    return None


def _extract_topic(lines: list[str]) -> str:
    for line in lines:
        if "topic of" in line:
            m = re.search(r"topic of \[(.*?)\]", line)
            if m:
                return m.group(1).strip()
            break

    for line in lines:
        s = line.strip()
        if not s or s == "--":
            continue
        if re.search(r"[\u4e00-\u9fff]", s):
            return s

    return ""


def _extract_questions(lines: list[str]) -> list[str]:
    pref: list[str] = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("--"):
            break
        pref.append(s)

    en_lines = [s for s in pref if re.search(r"[A-Za-z]", s)]
    if not en_lines:
        return []

    joined: list[str] = []
    i = 0
    while i < len(en_lines):
        cur = _norm_q(en_lines[i])

        while i + 1 < len(en_lines):
            nxt = _norm_q(en_lines[i + 1])
            if cur.endswith(("?", ".")):
                break
            if re.match(r"^[a-z]", nxt) or cur.lower().endswith(("by", "written", "the", "a", "an", "of", "to", "for", "in", "on")):
                cur = _norm_q(f"{cur} {nxt}")
                i += 1
                continue
            break

        joined.append(cur)
        i += 1

    # de-dup preserve order
    out: list[str] = []
    seen: set[str] = set()
    for q in joined:
        key = _norm_q(q)
        if key in seen:
            continue
        seen.add(key)
        out.append(q)
    return out


def _translate_question(en: str) -> str:
    key = _norm_q(en)
    return TRANSLATIONS.get(key, "（缺少翻译，请补充）")


def _extract_reason_fallback(lines: list[str], which: int) -> str:
    if which == 1:
        for line in lines:
            m = re.search(r"This is because\s+(.*?)(?:\.|$)", line, re.IGNORECASE)
            if m:
                return m.group(1).strip()
        for line in lines:
            m = re.search(r"\bis that\s+(.*?)(?:\.|$)", line, re.IGNORECASE)
            if m:
                return m.group(1).strip()
        return ""

    for line in lines:
        m = re.search(r"another obvious reason is that\s+(.*?)(?:\.|$)", line, re.IGNORECASE)
        if m:
            return m.group(1).strip()

    invest = next((l.strip() for l in lines if "renewable energy" in l.lower()), "")
    aware = next((l.strip() for l in lines if "public awareness" in l.lower()), "")
    if invest and aware:
        invest = re.sub(r"^For example,\s*", "", invest, flags=re.IGNORECASE).rstrip(".").strip()
        aware = re.sub(r"^In addition,\s*", "", aware, flags=re.IGNORECASE).rstrip(".").strip()
        return f"{invest}; {aware}"

    for line in lines:
        m = re.search(r"\bis that\s+(.*?)(?:\.|$)", line, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return ""


def build_cards_md(src_path: Path) -> str:
    text = src_path.read_text(encoding="utf-8", errors="ignore")
    sections = _split_sections(text)

    rows: list[tuple[int, str, list[str], str, str, str]] = []
    for num, lines in sections:
        topic = _extract_topic(lines)
        questions = _extract_questions(lines)

        stance = _extract_stance(lines) or ""
        reason1 = _extract_reason(lines, "believe that") or ""
        reason2 = _extract_reason(lines, "pointed out that") or ""

        if not reason1:
            reason1 = _extract_reason_fallback(lines, which=1)
        if not reason2:
            reason2 = _extract_reason_fallback(lines, which=2)
        rows.append((num, topic, questions, stance, reason1, reason2))

    md: list[str] = []
    md.append("# WE 题库要点卡片（从 预测题库/WE.txt 自动提取）")
    md.append("")
    md.append("用法：每题只背 3 件事：`立场(stance)` + `理由1` + `理由2`。例子统一用你自己的 2-3 个万能例子即可。")
    md.append("")

    for num, topic, questions, stance, reason1, reason2 in rows:
        md.append(f"## {num}. {topic}")
        if questions:
            md.append("- Questions:")
            for q in questions:
                md.append(f"  - EN: {q}")
                md.append(f"    ZH: {_translate_question(q)}")
        md.append(f"- Stance: {stance or '(choose one)'}.")
        md.append(f"- Reason 1: {reason1}.")
        md.append(f"- Reason 2: {reason2}.")
        md.append("")

    return "\n".join(md).rstrip() + "\n"


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    src = base_dir / "WE.txt"
    out = base_dir / "WE_要点卡片.md"

    out.write_text(build_cards_md(src), encoding="utf-8")
    print(f"Wrote: {out}")


if __name__ == "__main__":
    main()
