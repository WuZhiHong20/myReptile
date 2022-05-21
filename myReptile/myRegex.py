import re


def get_org(content):
    pattern = r'([\u4e00-\u9fa5]*)(\u53a6\u95e8)([\u4e00-\u9fa5]*)(\s|)([0-9]*)([\u4e00-\u9fa5]*)'
    org = re.search(pattern, content, re.U)
    if org:
        return org.group()
    return None


def get_tel(content) -> list:
    pattern = r'(([\u4e00-\u9fa5])*(\s)*)([\u4e00-\u9fa5])(:|：)((((\d{11})|((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})))(\s*)(,|，))*)((\d{11})|((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})))'
    res = []
    s = re.search(pattern, content, re.U)
    if not s:
        return []
    ss = s.group()  # 返回整个匹配的结果
    while True:
        res.append(ss)
        content = content[s.end():]
        if re.search(pattern, content, re.U) is None:
            break
        s = re.search(pattern, content, re.U)
        ss = s.group()
    return res
