## 1. Appending ##

/home/dq$ echo "take one down, pass it aroynd, 98 bottles of beer on

## 2. Redirecting from a file ##

/home/dq$ sort -r < beer.txt

## 3. The grep command ##

/home/dq$ grep "bottles of" beer.txt coffee.txt

## 4. Special characters ##

/home/dq$ grep "beer" beer?.txt

## 5. The star wildcard ##

/home/dq$ grep "beer" *.txt

## 6. Piping output ##

/home/dq$ python love.py | grep l

## 7. Chaining commands ##

/home/dq$ echo "all beers are gone" >> beer.txt && cat beer.txt

## 8. Escaping characters ##

/home/dq$ echo "\"o home.\" lily said" >> quato.txt