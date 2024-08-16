from flask import Flask, render_template, request

app = Flask(__name__)

# Gimatria function to calculate the Gimatric value of a word
def gimatria(word):
    # Hebrew letter to number mapping
    letter_values = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 10, 'כ': 20, 'ך': 20,  'ל': 30, 'מ': 40,'ם': 40, 'נ': 50,'ן': 50, 'ס': 60, 'ע': 70, 'פ': 80,'ף': 80, 'צ': 90,'ץ': 90,
        'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
    }
    
    # Calculate the Gimatric value of the word
    value = sum(letter_values.get(char, 0) for char in word)
    gvalue=value
    # Reduce the value to a single digit
    while value >= 10:
        value = sum(int(digit) for digit in str(value))
    
    return gvalue, value

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    gtext = ''
    gsum = 0
    gsumz = 0
    text = ''  # Initialize text here

    if request.method == 'POST':
        text = request.form.get('hebrew_text', '')
        if text:
            gtext = text
            words = text.split()
            gsum = 0
            for word in words:
                gw = gimatria(word)
                result[word] = gw
                gsum += gw[0]
            gsumz = gsum
            while gsumz >= 10:
                gsumz = sum(int(digit) for digit in str(gsumz))

    return render_template('index.html', text=gtext, gsum=(gsum, gsumz), result=result)
if __name__ == '__main__':
    app.run(debug=True)
