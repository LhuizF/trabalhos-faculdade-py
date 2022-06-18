class Pessoa:
  name = ''
  doc = 0
  age = 0
  next = None

  def __init__(self, name, doc, next):
    self.name = name
    self.doc = doc
    self.next = next

class Fila_prioritaria:
  first = None
  last = None
  total = 0

  def __init__(self):
    pass

  def add_end(self, name, doc):
    new_node = Pessoa(name, doc, None)
    if self.first == None and self.last == None:
      self.first = new_node
      self.last = new_node
      self.total += 1
      return

    aux = self.last
    aux.next = new_node
    self.last = new_node
    self.total += 1

class Fila_grande_publico:
  first = None
  last = None
  total = 0

  def __init__(self):
    pass

  def add_end(self, name, doc):
    new_node = Pessoa(name, doc, None)
    if self.first == None and self.last == None:
      self.first = new_node
      self.last = new_node
      self.total += 1
      return

    aux = self.last
    aux.next = new_node
    self.last = new_node
    self.total += 1

class Vaccine_box:
  amount = 0
  next_box = None

  def __init__(self, amount, next_box):
    self.amount = amount
    self.next_box = next_box

class Vaccine_queue:
  first = None
  last = None
  total_box = 0

  def __init__(self):
    pass

  def add(self, amount):
    new_vaccine_box = Vaccine_box(amount, None)
    if self.first == None and self.last == None:
      self.first = new_vaccine_box
      self.last = new_vaccine_box
      self.total_box += 1
      return

    aux = self.last
    aux.next_box = new_vaccine_box
    self.last = new_vaccine_box
    self.total_box += 1

class Queue:
  main_queue = Fila_grande_publico()
  priority_queue = Fila_prioritaria()
  vaccine_queue = Vaccine_queue()

  def __init__(self):
    pass

  def add(self, name, doc, age):
    # não sei a idade exata para entra na fila de prioridade prioritaria :/
    if age < 50:
      self.main_queue.add_end(name, doc)
    else:
      self.priority_queue.add_end(name, doc)

  def print(self):
    print('----------------------------------------------------')
    print('Total de caixas:', self.vaccine_queue.total_box)
    print('Total de vacinas na caixa aberta:', self.vaccine_queue.first.amount)

    total_vaccine = 0
    aux = self.vaccine_queue.first
    
    while aux != None:
      total_vaccine += aux.amount
      aux = aux.next_box

    print('Total de vacinas em todas as caixas:', total_vaccine)

    self.print_queue(self.main_queue, 'Fila grande publico')
    self.print_queue(self.priority_queue, 'Fila prioritária')
    print('----------------------------------------------------')

  def add_vaccine_box(self, amount):
    if amount == 0:
      print('Você não pode adicionar um caixa vazia')
      return
    self.vaccine_queue.add(amount)

  def print_queue(self, queue, queue_name):
    aux = queue.first
    i = 1
    print(queue_name)
    while aux != None:
      print(i, aux.name, aux.doc)
      aux = aux.next
      i += 1
    print('Total na ', queue_name,":", queue.total)
    print('\n')

  def apply_vaccine(self):
    queue = self.priority_queue

    if queue.first == None:
      print('Fila de prioridade vazia')
      print('Aplicando vacina na fila de grande publico')
      queue = self.main_queue

      if queue.first == None:
        print('Fila grande publico vazia')

    patient = queue.first
    box = self.vaccine_queue.first

    if box == None:
      print('Não há caixas disponíveis')
      return

    if box.amount == 0:
      print('Caixa atual vazia')
      if box.next_box == None:
        self.vaccine_queue.total_box -= 1
        print('Não há mais caixas para abrir')
        return
      print('Abrindo uma nova caixa')
      self.vaccine_queue.total_box -= 1
      self.vaccine_queue.first = box.next_box
      box = box.next_box


    if box.amount > 0 and patient != None:
      box.amount -= 1
      queue.total -= 1
      queue.first = patient.next
      print('Aplicando vacina para', patient.name)
      return

    print('Não há mais pacientes para aplicar vacina')

lista = Queue()

# 1-2 Adicionando pacientes
lista.add('João', 3551, 20)
lista.add('Maria', 3552, 49)
lista.add('José', 3553, 56)

# 3 Adicionando caixas com a quantidade de vacinas
lista.add_vaccine_box(5)
lista.add_vaccine_box(20)


# 4 Aplicando vacina
lista.apply_vaccine()
lista.apply_vaccine()
lista.apply_vaccine()

# 5 exibindo estatísticas
lista.print()
