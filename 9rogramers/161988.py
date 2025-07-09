def solution(sequence):
    pulse = [1,-1]
    
    n_sequence = [pulse[i%2-1]*sequence[i] for i in range(len(sequence))]
    p_sequence = [pulse[i%2]*sequence[i] for i in range(len(sequence))]
    dp_n=[0]*len(sequence)
    dp_p=[0]*len(sequence)
    
    dp_n[0] = n_sequence[0]
    dp_p[0] = p_sequence[0]

    for i in range(1,len(n_sequence)):
        dp_n[i] = max(n_sequence[i],dp_n[i-1]+n_sequence[i])
        dp_p[i] = max(p_sequence[i],dp_p[i-1]+p_sequence[i])
        

    return max(dp_n+dp_p)