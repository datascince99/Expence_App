def calculate_splits(expense, splits_data):
    splits = []
    total_amount = expense['amount']

    if expense['split_method'] == 'equal':
        num_participants = len(splits_data)
        equal_amount = total_amount / num_participants
        for data in splits_data:
            splits.append({'user_id': data['user_id'], 'amount': equal_amount})

    elif expense['split_method'] == 'exact':
        for data in splits_data:
            splits.append({'user_id': data['user_id'], 'amount': data['amount']})

    elif expense['split_method'] == 'percentage':
        for data in splits_data:
            amount = total_amount * (data['percentage'] / 100)
            splits.append({'user_id': data['user_id'], 'amount': amount, 'percentage': data['percentage']})

    return splits
