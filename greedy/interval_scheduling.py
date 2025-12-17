def penjadwalan(A):
    # urutkan berdasarkan waktu yang paling cepat selesai
    A.sort(key=lambda x:x[1])
    
    
    # kalau jadwal kosong
    if not A:
        return 0
        
    end_limit = A[0][1]
    count = 1
    
    for i in range(1,len(A)):
        current_start = A[i][0]
        current_end = A[i][1]
        
        if current_start > end_limit:
            count += 1
            end_limit = current_end
            
    return count


soal1 =[[1,4],[3,9],[4,8],[10,15],[16,18],[18,24]]
jawaban = penjadwalan(soal1)
print(jawaban)
