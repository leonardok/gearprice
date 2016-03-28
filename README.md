## Setup

	bash ./bootstrap.sh
	source activate-filter

	export DATABASE_URL="sqlite:////tmp/db.sqlite3"
	export DATABASE_URL="postgres://postgres:user@localhost:5432/database"
	export CLOUDINARY_URL="cloudinary://cloudinary_url"

	./manage.py syncdb
	./manage.py migrate
	./manage.py collectstatic

	# a better server
	./manage.py runserver 0.0.0.0:5000

	python manage.py shell_plus --ipython
