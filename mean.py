def get_mean(norm_value=255, dataset='activitynet'):
    assert dataset in ['activitynet', 'kinetics','cichlids']

    if dataset == 'activitynet':
        return [
            114.7748 / norm_value, 107.7354 / norm_value, 99.4750 / norm_value
        ]
    elif dataset == 'kinetics':
        # Kinetics (10 videos for each class)
        return [
            110.63666788 / norm_value, 103.16065604 / norm_value,
            96.29023126 / norm_value
        ]
    elif dataset == 'cichlids':
        # Kinetics (10 videos for each class)
        return [
            76.20589554918055 / norm_value, 80.90237506210525 / norm_value,
            76.79881159479473 / norm_value
        ]



def get_std(norm_value=255, dataset='activitynet'):
    if dataset == 'cichlids':
        return [
            43.02384117950772 / norm_value, 45.245146004359434 / norm_value,
            44.903208894140846 / norm_value
        ]
    # Kinetics (10 videos for each class)
    else:
        return [
            38.7568578 / norm_value, 37.88248729 / norm_value,
            40.02898126 / norm_value
        ]
    
