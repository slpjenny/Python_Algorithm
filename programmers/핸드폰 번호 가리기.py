def solution(phone_number):
    front = phone_number[:-4:]
    back = list(phone_number[-4::])
    new_front = []

    front = list(front)
    for i in front:
        new_front.append('*')

    phone_number = new_front+back
    return "".join(phone_number)
