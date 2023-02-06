from datetime import date
import os


def get_month():
    return date.today().strftime('%B')


def get_year():
    return date.today().strftime('%Y')


def display_options():
    print('Clocking out? type 1')
    print('Need a report? type 2')
    print('Exit. type 3')


def get_option_input():
    return input('Enter an option: ')


def clock_out():
    path = os.path.expanduser(f'~/.punchcard/{get_month()}_{get_year()}.txt')
    with open(path, 'a') as pc:
        project = input('Project Name: ')
        hours = input('Project hours: ')
        pc.write(f'{project}: {hours}\n')


def add_to_dict(line, dict):
    key = line.split()[0]
    hours = line.split()[1]
    if key in dict:
        dict[key] = dict.get(key) + int(hours)
    else:
        dict[key] = int(hours)
    return dict


def gen_report():
    hours_by_project = {}
    path = os.path.expanduser(f'~/.punchcard/{get_month()}_{get_year()}.txt')
    with open(path) as pc:
        for line in pc:
            hours_by_project = add_to_dict(line, hours_by_project)

    print(hours_by_project)


def exit_punchcard():
    print('Exited')


def main():
    display_options()
    input = get_option_input()

    if input == '1':
        clock_out()
    elif input == '2':
        gen_report()
    elif input == '3':
        exit_punchcard()


if __name__ == "__main__":
    main()
