class Yacht:

    textKind = [
        'Aces',
        'Deuces',
        'Threes',
        'Fours',
        'Fives',
        'Sixes',
    ]

    textSubtotal = [
        'Subtotal',
        '+35 Bonus',
    ]

    textMix = [
        'Choice',
        '4 of a Kind',
        'Full House',
        'S. Straight',
        'L. Straight',
        'Yacht',
    ]

    textTotal = [
        'Total',
    ]

    allYacht = {}

    for i in range(6):
        allYacht[textKind[i]] = i
    for i in range(2):
        allYacht[textSubtotal[i]] = 6+i
    for i in range(6):
        allYacht[textMix[i]] = 8+i
    allYacht[textTotal[0]] = 14