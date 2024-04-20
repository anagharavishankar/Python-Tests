if __name__ == '__main__':
    monthly_expense = [2200, 2350, 2600, 2130, 2190]

    # 1. In Feb, how many dollars you spent extra compare to January?
    print(monthly_expense[1] - monthly_expense[0])

    # 2. Find out your total expense in first quarter (first three months) of the year.
    print(sum(monthly_expense[0:3]))

    # 3. Find out if you spent exactly 2000 dollars in any month
    if 2000 in monthly_expense:
        print("Spent 2000")
    else:
        print("2000 is not spent")

    # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    monthly_expense.append(1980)

    # 5. You returned an item that you bought in a month of April and
    #    got a refund of 200$. Make a correction to your monthly expense list
    #    based on this
    monthly_expense.pop(3)
    monthly_expense.insert(3, 2130-200)

    print("Final monthly expense list is: ", monthly_expense)
