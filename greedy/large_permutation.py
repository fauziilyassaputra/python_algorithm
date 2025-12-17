def largest_permutation(A,B):
    # batas looping
    i = 0
    
    # angka terbesar
    max_number = len(A)
    
    # buat peta (kasih index di tiap angka)
    map_number = {v:i for i, v in enumerate(A)}
    
    # pengecekan
    while B and i < len(A):
        target_number = map_number[max_number]
        if i == target_number:
            pass
        else:
            B -= 1
            A[i], A[target_number] = A[target_number], A[i]
            map_number[A[i]], map_number[A[target_number]] = map_number[A[target_number]], map_number[A[i]]
        i += 1
        max_number -= 1
            
    return A
            
soal1 = [4,2,5,1,6,7,9,8,3]
batas1 = 3

soal2 = [3,5,2,4,1]
batas2 = 2

jawaban1 = largest_permutation(soal1,batas1)
jawaban2 = largest_permutation(soal2, batas2)

print(jawaban1)
print(jawaban2)
            
