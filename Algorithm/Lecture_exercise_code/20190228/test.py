boards = Board.objects.all()

boards = Board.objects.filter(title='hello').all()
boards = Board.objects.filter(title='hello').first()

board = Board.objects.get(pk=1)

board = Board.objects.filter(id=1)

boards = Board.objects.filter(title__contains='he').all()
boards = Board.objects.filter(content__startswith='he')
boards = Board.objects.filter(content__endswith='!')

boards = Board.objects.order_by('title').all()
boards = Board.objects.order_by('-title')