from django.shortcuts import render

# Create your views here.
def history(request):
    return render(request, 'history.html', {'history_game': history_game})

history_game = []
moves = 0

secret_num = [4,5,6,7]

def bulls_cow(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        num = request.POST.get('numbers')
        contex = {}
        if num:
            try:
                numbers = list(map(int, num.split()))
                bulls, cows = guess_numbers(secret_num, numbers)
                if bulls == len(secret_num):
                    contex['message'] = 'You got it! You WIN!'
                else:
                    contex['message'] = f'You got {bulls} bulls and {cows} cows.'
                global moves
                moves += 1
                history_game.append({'id': moves, 'bulls': bulls, 'cows': cows})
            except ValueError:
                contex['message'] = 'Enter the number not string'
        else:
            contex['message'] = 'Please enter the number '
        return render(request, 'index.html', contex)



def guess_numbers(secret, numbers):
    bulls = 0
    cows = 0
    resp = 'Wrong numbers'
    if len(numbers) != len(secret):
        return resp
    for i in range(len(secret)):
        if numbers[i] == secret[i]:
            bulls += 1
        elif numbers[i] in secret:
            cows += 1
    return bulls, cows
