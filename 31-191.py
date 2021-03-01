def main():
    F_n = int(input("Inserire valore fatturato zona n: "))
    F_c = int(input("Inserire valore fatturato zona c: "))
    F_s = int(input("Inserire valore fatturato zona s: "))
    F_i = int(input("Inserire valore fatturato zona i: "))

    F_tot = F_n + F_c + F_s + F_i
    f_perc_n = F_n*100/F_tot
    f_perc_c = F_c*100/F_tot
    f_perc_s = F_s*100/F_tot
    f_perc_i = F_i*100/F_tot

    print("Per la parte nord il fatturato è:", F_n, "ed è il", f_perc_n, "% del totale.")
    print("Per la parte nord il fatturato è:", F_c, "ed è il", f_perc_c, "% del totale.")
    print("Per la parte nord il fatturato è:", F_s, "ed è il", f_perc_s, "% del totale.")
    print("Per la parte nord il fatturato è:", F_i, "ed è il", f_perc_i, "% del totale.")

main()