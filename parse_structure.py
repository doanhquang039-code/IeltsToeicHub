from html.parser import HTMLParser

class StructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.log = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        tag_id = attrs_dict.get('id', '')
        tag_cls = attrs_dict.get('class', '')
        info = f"{tag}"
        if tag_id: info += f"#{tag_id}"
        if tag_cls: info += f".{tag_cls.replace(' ', '.')}"
        
        # void tags
        if tag in ['img', 'input', 'br', 'hr', 'meta', 'link']:
            return
            
        self.stack.append(info)
        if 'view' in tag_cls or tag in ['aside', 'main', 'header']:
            parents = " > ".join([s.split('.')[0] for s in self.stack[:-1]])
            print(f"OPEN  {info:35} | PARENTS: {parents}")

    def handle_endtag(self, tag):
        if tag in ['img', 'input', 'br', 'hr', 'meta', 'link']:
            return
        # pop matching tag
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i].split('#')[0].split('.')[0] == tag:
                popped = self.stack.pop(i)
                if 'view' in popped or tag in ['aside', 'main']:
                    print(f"CLOSE {popped:35}")
                break

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

parser = StructureParser()
parser.feed(html)
