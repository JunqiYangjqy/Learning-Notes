class algorithms:
    #insertion sort
    def insert_sort(lista):
        for j in range(1,len(lista)):
            key=lista[j]
            i=j-1
            while i>=0 and lista[i]>key:
                lista[i+1]=lista[i]
                i=i-1
            lista[i+1]=key
        return lista

    def insert_sort_reverse(listA):
        """Reverse"""
        for i in range(1, len(listA)):
            for j in range(i,0,-1):
                if listA[j] < listA[j-1]:
                    listA[j], listA[j-1] = listA[j-1], listA[j]
                else:
                    break
        return listA
