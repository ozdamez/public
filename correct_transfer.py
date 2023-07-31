while True:
	file_name = input('Wpisz nazwe pliku:')
	try:
		fh = open(file_name).read()
		break
	except:
		input("Nie udalo sie otworzyc plik. Sprawdz nazwe i sprobuj jeszcze raz.")
fh = fh.split('\n')
#print(*fh)
output_file = ''
for line in range(len(fh)):
    #print(line)
    if fh[line].startswith(':32A:'):
        day = fh[line][4:10]
        output_file += fh[line] + '\n'
    if fh[line].startswith(':50'):
        output_file += fh[line] + '\n' + fh[line + 1] + '\n' + fh[line + 2] + '\n'
    if fh[line].startswith(':52'):
        output_file += ':52D:' + fh[line][10:] + '\n' + fh[line][10:] + '\n' + '\n' + '            ' + fh[line + 3][5:7] + ' ' + fh[line + 3][5:7] +  '\n'
    if fh[line].startswith(':57A:'):
        output_file += fh[line] + '\n' + '\n'
    if fh[line].startswith(':59:'):
        output_file += fh[line][:8] + fh[line][10:]+ '\n'
        output_file += fh[line + 1] + '\n' + fh[line + 2] + '\n' + fh[line + 3] + '\n' + fh[line + 4] + '\n'
    if fh[line].startswith(':70:'):
        output_file += fh[line] + '\n' + ':71A:BN1' + '\n' + ':72:' + '\n'
    

export_file = 'converted_' + file_name.strip()
ef = open(export_file, 'w')
ef.write(output_file)
ef.close()
out = input('Wykonane! PRESS ENTER')