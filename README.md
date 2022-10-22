# InfoConcert

You would like to know the concert near your town ? But only concert of your artist ? Or from the french web radio [FIP](https://www.radiofrance.fr/fip) ?
This programm look for concert near of your town in the website [InfoConcert](https://www.infoconcert.com/), and filter them by your artists in your musique folder or from artists from the webradio [FIP](https://www.radiofrance.fr/fip).

## Instalation
```
pip install -r requirements.txt
```
Or if your are using 'pipenv'
```
pipenv shell
pipenv install
```
## How to ? 
For artist in your librairy : 
```
python main.py --departement 13 
```
You may need to add `--path "YOUR PATH TO YOUR MUSIC FOLDER"`

For artist from the radios fip
```
python main.py --departement 13 --fip
```

If you want to receive a message on your telegram account, add `--telegram` (your should configure with `telegram-send --configure` before) 