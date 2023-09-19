import csv  
def main():  
    # Para abrir el archivo CSV 
    with open(' python.csv ', newline = '') as csv_file:  
        csv_read = csv.reader( csv_file, delimiter = ',')  
  
        # Para leer y mostrar cada fila 
        for row in csv_read:  
            print(row)  
if __name__ == '__main__':  
    main()  
