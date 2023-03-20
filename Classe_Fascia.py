# Classe che rappresente la fascia oraria in cui inserire i programmi

class Fascia:
    def __init__(self, nome, num_slot, inizio):
        self.nome = nome
        self.num_slot = num_slot
        self.durata = int(num_slot * 30)
        self.inizio = inizio
