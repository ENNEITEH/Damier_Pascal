# The Pascal Tiling

(La version française est disponible ci-dessous)

![The Pascal Tiling Conjecture](./PascalTilingConjecture.png)

![Building the Pascal Tiling](./BuildingPascalTiling.png)

This repository presents my work on a conjecture linking the properties of Pascal's triangle and prime numbers.

This project began in April 2025, as part of the preparation for the *Grand Oral* exam of the French Baccalauréat.

Pascal's triangle is known for exhibiting surprising structures when represented modulo $q$, where $q$ is a prime number.

Representation of Pascal's triangle modulo 2 for $N=128$:

![Pascal Triangle N=128 modulo 2](./examples/PascalFractal_128_mod_2.png)

While manipulating the first $N$ rows of Pascal's triangle and reducing them modulo $N$, I observed a regular structure when $N$ is a prime number, while the structure appears irregular when $N$ is not prime.

The Pascal Tiling is **regular** for the prime number $N=37$:

![Pascal Tiling N=37 modulo 37](./examples/DamierPascal_37.png)

The Pascal Tiling is **not regular** for the non-prime number $N=32$:

![Pascal tiling N=32 modulo 32](./examples/DamierPascal_32.png)

To build the desired square matrix of size N×N, we start by extracting the first N rows of Pascal’s Triangle in left-aligned "staircase" form. These rows are used to create the upper triangle of a matrix, which is then completed by diagonal symmetry (with respect to the main diagonal).

To obtain a second matrix, we take the first N right-aligned rows of Pascal’s Triangle. We reverse the order of the rows: the first becomes the last, the second becomes the second-to-last, and so on, effectively creating a vertically reflected version. This matrix is also completed by diagonal symmetry.

By adding these two matrices together, we obtain the final N×N square matrix. This matrix is used to generate an image: we place a black pixel when the value is a multiple of N, and a white pixel otherwise.

We define a regular Pascal Tiling by two rules:

- The top-left pixel is white.
- Every pixel is surrounded (horizontally and vertically) by pixels of the opposite color: a white pixel can only touch black pixels, and vice versa.

From this, the following equivalence emerges:

**For N > 2, N is prime if and only if the resulting Tiling is regular.**

When $N$ is not prime, the tiling is irregular and shows patterns resembling the fractal-like structures typically observed in Pascal's triangle modulo $q$.

The proof of this conjecture is currently under review. After this review, the Pascal Tiling Conjecture will become a theorem.

[Introduction_EN](./introduction_EN.ipynb)

# Le Damier de Pascal

![La Conjecture du Damier de Pascal](./PascalTilingConjecture.png)

![La construction du Damier de Pascal](./BuildingPascalTiling.png)

Ce dépôt présente mon travail sur une conjecture liant les propriétés du triangle de Pascal et les nombres premiers.

Ce travail a débuté en Avril 2025, à l'occasion de la préparation du Grand Oral des épreuves du baccalauréat.

Le triangle de Pascal est connu pour faire apparaître de nombreuses structures étonnantes lorsqu'on le représente modulo $q$ où $q$ est un nombre premier.

Représentation du triangle de Pascal modulo 2 pour  $N=128$.

![Triangle Pascal N=128 modulo2](./examples/PascalFractal_128_mod_2.png)


En manipulant les $N$ premières lignes du triangle de Pascal, et en prenant le modulo $N$ , j'ai vu apparaitre une structure régulière lorsque $N$ est un nombre premier, alors que la structure reste irrégulière lorsque $N$ n'est pas un nombre premier.

Le Damier de Pascal **est régulier** pour le nombre premier $N=37$.

![Damier de Pascal N=37 modulo 37](./examples/DamierPascal_37.png)

Le Damier de Pascal **n'est pas régulier** pour le nombre premier $N=32$.

![Damier de Pascal N=32 modulo 32](./examples/DamierPascal_32.png)


Pour construire la matrice carrée de dimension N×N souhaitée, on commence par extraire les N premières lignes du Triangle de Pascal en forme d’escalier, aligné à gauche. Ces lignes servent à former une première matrice, que l’on complète par une symétrie diagonale (par rapport à la diagonale principale).

Pour obtenir une seconde matrice, on considère cette fois les N premières lignes du Triangle de Pascal aligné à droite. On inverse alors l’ordre des lignes : la première devient la dernière, la deuxième devient l’avant-dernière, et ainsi de suite, jusqu’à obtenir une version reflétée verticalement. que l’on complète également par une symétrie diagonale (par rapport à la diagonale principale).

C'est en additionnant les deux matrices que l'on obtient notre matrice carrée de dimensions NxN. Cette matrice nous permet de créer des images ou l'on mettra un pixel noir quand l'on tombe sur un multiple de N et un pixel noir quand le nombre n'est pas un multiple. 

On définie un Damier régulier par 2 règles:

- Le pixel en haut à gauche est blanc
- Tous les pixels sont entourés verticalement et horizontalement par des pixels de couleur opposée : un pixel blanc ne peut être adjacent qu’à des pixels noirs, et inversement.

Il en découle l'équivalence suivante:

**Pour N>2, N est premier si et seulement si on obtient un Damier régulier**

Lorsque $N$ n'est pas premier, la Damier est irrégulier et laisse apparaître une structure proche des structures fractales habituellement observées avec le triangle de Pascal modulo q.

Cette demonstration est soumise à une relecture. À l'issue de cette relecture, cette conjecture deviendra un théorème.

[Introduction_FR](./introduction_FR.ipynb)
