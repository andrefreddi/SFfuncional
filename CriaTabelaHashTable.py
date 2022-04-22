class HashTable:

	# Cria uma lista de buckets vazia de determinado tamanho
	def __init__(self, size):
		self.size = size
		self.hash_table = self.create_buckets()

	def create_buckets(self):
		return [[] for _ in range(self.size)]

	# Insere valores no hashmap
	def set_val(self, key, val):
		
		# Busca o índice da chave usando a função hash
		hashed_key = hash(key) % self.size
		
		#Busca o bucket correspondente ao índice
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# verifique se o bucket tem a mesma chave
      # que a chave a ser inserida
			if record_key == key:
				found_key = True
				break

		# Se o bucket tiver a mesma chave que a chave
    # a ser inserida, atualizar o valor da chave
		# Se não tive, anexe o novo par de valores-chave ao bucket
		if found_key:
			bucket[index] = (key, val)
		else:
			bucket.append((key, val))

	# Retornar valor pesquisado com chave específica
	def get_val(self, key):
		
		# Busca o índice da chave usando função hash
		hashed_key = hash(key) % self.size
		
		# Busca o bucket correspondente ao índice
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# verifique se o bucket tem a mesma chave
      # que a chave que está sendo pesquisada
			if record_key == key:
				found_key = True
				break

		# Se o bucket tiver a mesma chave que a chave que
    # está sendo pesquisada, retorna o valor encontrado.
		# Se não tiver, indica que não foi encontrado nenhum registro
		if found_key:
			return record_val
		else:
			return "No record found"

	# Remover um valor com chave específica
	def delete_val(self, key):
		
		# Busca o índice da chave usando função hash
		hashed_key = hash(key) % self.size
		
		# Busca o bucket correspondente ao índice
		bucket = self.hash_table[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			# verifique se o bucket tem a mesma chave
      # que a chave a ser excluída
			if record_key == key:
				found_key = True
				break
		if found_key:
			bucket.pop(index)
		return

	# Para imprimir os itens do hash map
	def __str__(self):
		return "".join(str(item) for item in self.hash_table)

hash_table = HashTable(1)