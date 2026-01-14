'''
chapter07_hangman 내에 hangman_complete 패키지 생성
hangman06.py을 옮기겠습니다.

hangman_arts.py 파일 생성       -> hangman05.py에 있던 logo / stages를 복사
hangman_word_list.py 파일 생성  -> hangman05.py에 있던 word_list를 복사

그리고 나머지 부분을 hangman06.py에 전부 복사
'''
word_list = [
    # 1-50
    "apple", "banana", "camel", "doctor", "elephant", "forest", "guitar", "house", "island", "jacket",
    "kangaroo", "lemon", "mountain", "notebook", "orange", "pencil", "queen", "rabbit", "school", "tiger",
    "umbrella", "valley", "window", "xylophone", "yellow", "zebra", "airport", "bridge", "camera", "dinner",
    "energy", "flower", "garden", "hammer", "insect", "jungle", "kitchen", "laptop", "market", "nature",
    "ocean", "palace", "quiet", "river", "summer", "ticket", "uncle", "village", "winter", "yogurt",

    # 51-100
    "animal", "bottle", "coffee", "desert", "engine", "family", "global", "health", "image", "journey",
    "knight", "library", "memory", "number", "office", "person", "quartz", "reason", "silver", "theory",
    "update", "visual", "weather", "young", "zenith", "active", "bright", "clever", "danger", "effect",
    "famous", "gentle", "hungry", "impact", "joyful", "kindly", "lovely", "modern", "narrow", "online",
    "polite", "quick", "remote", "strong", "travel", "unique", "vacuum", "weekly", "yearly", "zealous",

    # 101-150
    "action", "beauty", "circle", "degree", "entire", "future", "growth", "history", "inside", "junior",
    "keeper", "lesson", "method", "nation", "object", "player", "quality", "result", "simple", "target",
    "useful", "volume", "worker", "action", "beyond", "center", "direct", "effort", "figure", "ground",
    "height", "income", "justice", "knowledge", "liquid", "moment", "notice", "option", "period", "record",
    "source", "talent", "urgent", "valley", "weight", "accept", "become", "change", "decide", "expect",

    # 151-200
    "follow", "happen", "ignore", "judge", "listen", "manage", "notice", "obtain", "permit", "reduce",
    "select", "travel", "understand", "verify", "wonder", "appear", "belong", "create", "depend", "expand",
    "forget", "gather", "handle", "inform", "launch", "modify", "occupy", "prefer", "remain", "spread",
    "target", "unite", "vanish", "within", "accept", "border", "common", "damage", "energy", "factor",
    "guilty", "honest", "island", "leader", "manner", "native", "output", "proper", "random", "safety",

    # 201-250
    "theory", "useful", "victim", "wealth", "ability", "balance", "canvas", "detail", "expert", "flavor",
    "glance", "hollow", "injury", "jumper", "kettle", "luxury", "magnet", "nephew", "origin", "planet",
    "rhythm", "spirit", "tablet", "unique", "vessel", "wisdom", "anchor", "button", "castle", "device",
    "evolve", "frozen", "galaxy", "hazard", "indoor", "jockey", "kidney", "layout", "museum", "nephew",
    "oxygen", "purity", "recipe", "sphere", "tunnel", "update", "visual", "walnut", "yield", "zodiac",

    # 251-300
    "absent", "behind", "column", "detect", "enable", "flight", "guider", "health", "invest", "jumper",
    "layout", "mental", "nearby", "object", "parent", "really", "screen", "though", "useful", "versus",
    "window", "across", "bottom", "custom", "design", "escape", "format", "global", "hybrid", "ignore",
    "jacket", "layout", "matrix", "normal", "output", "patent", "rating", "series", "timing", "unless",
    "volume", "weapon", "yellow", "asleep", "better", "cloudy", "driver", "enough", "forget", "guitar"
]