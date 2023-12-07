# part 1

from collections import Counter

with open("./day7/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day7/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

hands = [[line.split(" ")[0], int(line.split(" ")[1])] for line in Lines]

for hand in hands:
    c = Counter(hand[0])
    hand.append(c.most_common())


# group hands in types
five = list()
four = list()
full_house = list()
three = list()
two_pair = list()
one_pair = list()
high_card = list()


for hand in hands:
    c = hand[2]

    # check for possible types
    if len(c) == 1:
        five.append(hand)

    elif len(c) == 2 and c[0][1] == 4:
        four.append(hand)

    elif len(c) == 2 and c[0][1] == 3:
        full_house.append(hand)

    elif len(c) == 3 and c[0][1] == 3:
        three.append(hand)

    elif len(c) == 3 and c[0][1] == 2:
        two_pair.append(hand)

    elif len(c) == 4:
        one_pair.append(hand)

    elif len(c) == 5:
        high_card.append(hand)


types = [five, four, full_house, three, two_pair, one_pair, high_card]

# introduce a sorting score that corresponds with the cards in hand
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
card_value = dict(zip(cards, range(2, 15)))

for typee in types:
    for hand in typee:
        score = [card_value[card] for card in hand[0]]
        score = (
            score[0] * pow(10, 8)
            + score[1] * pow(10, 6)
            + score[2] * pow(10, 4)
            + score[3] * pow(10, 2)
            + score[4]
        )
        hand.append(score)

    # sort by the newly created score
    typee.sort(key=lambda x: x[3])


order = [t[1] for typee in types[::-1] for t in typee if len(typee)]

result1 = 0
for factor, bid in enumerate(order):
    result1 += bid * (factor + 1)

print(f"{result1 = }")


# ---------------------------------------------------------
# part 2

# with open("./day7/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

hands = [[line.split(" ")[0], int(line.split(" ")[1])] for line in Lines]

for hand in hands:
    c = Counter(hand[0])
    hand.append(c.most_common())


# group hands in types
five = list()
four = list()
full_house = list()
three = list()
two_pair = list()
one_pair = list()
high_card = list()

for hand in hands:
    cards = hand[0]
    c = hand[2]
    Js = 0
    [Js := card[1] for card in c if card[0] == "J"]

    # updated check for possible types
    # Jokers always provide best option
    if (len(c) == 1) or (  # KKKKK
        len(c) == 2 and "J" in cards  # KKKKJ, KKKJJ, KKJJJ, KJJJJ, JJJJJ
    ):
        five.append(hand)

    elif (
        (len(c) == 2 and c[0][1] == 4)  # KKKKQ
        or ("J" in cards and len(c) == 3 and c[0][1] == 3)  # KKKQJ, KQJJJ
        or (Js == 2 and len(c) == 3)  # KKQJJ
    ):
        four.append(hand)

    elif (len(c) == 2 and c[0][1] == 3) or (  # KKQQQ
        "J" in cards and len(c) == 3  # KKQQJ
    ):
        full_house.append(hand)

    elif (len(c) == 3 and c[0][1] == 3) or (  # KKKAQ
        "J" in cards and len(c) == 4  # KKJAQ, KJJAQ
    ):
        three.append(hand)

    elif len(c) == 3 and c[0][1] == 2:  # KKQQT
        two_pair.append(hand)

    elif (len(c) == 4) or (len(c) == 5 and "J" in cards):  # AAKQT  # AKQTJ
        one_pair.append(hand)

    elif len(c) == 5:  # AKQT9
        high_card.append(hand)


types = [five, four, full_house, three, two_pair, one_pair, high_card]

cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
card_value = dict(zip(cards, range(2, 15)))

for typee in types:
    for hand in typee:
        score = [card_value[card] for card in hand[0]]
        score = (
            score[0] * pow(10, 8)
            + score[1] * pow(10, 6)
            + score[2] * pow(10, 4)
            + score[3] * pow(10, 2)
            + score[4]
        )
        hand.append(score)

    typee.sort(key=lambda x: x[3])


order = [t[1] for typee in types[::-1] for t in typee if len(typee)]

result2 = 0
for factor, bid in enumerate(order):
    result2 += bid * (factor + 1)

print(f"{result2 = }")
