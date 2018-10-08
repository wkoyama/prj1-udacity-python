import fresh_tomatoes
import media
from integration_apis import MovieDB

movies = []
populares = MovieDB().get_popular()

for pop in populares['results']:
    movie = media.Movie(pop)
    movies.append(movie)

# avengers_infinity_war = media.Movie("Vingadores: Guerra Infinita",
#                         "Homem de Ferro, Thor, Hulk e os Vingadores se unem para combater seu inimigo mais poderoso, o maligno Thanos. Em uma missão para coletar todas as seis pedras infinitas, Thanos planeja usá-las para infligir sua vontade maléfica sobre a realidade.",
#                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTP6Mg3v2AfdPxqsFG1_6U69knBhHzaK-ttGeHC5FER_ueTvsZSgFEUiWM",
#                         "http://www.youtube.com/watch?v=Aiv5sYzwGb8")

# clube_dos_cinco = media.Movie("Clube dos Cinco",
#                         "Cinco adolescentes do ensino médio cometem pequenos delitos na escola e, como punição, têm que passar o sábado no colégio e escrever uma redação contando o que pensam de si mesmos. O grupo reúne jovens com perfis completamente diferentes: o popular, a patricinha, a esquisita, o nerd e o rebelde. No decorrer do dia, eles passam a se conhecer melhor e a aceitar suas diferenças, compartilhando seus maiores segredos.",
#                         "http://t2.gstatic.com/images?q=tbn:ANd9GcRh3Rhuq986YXFFmgWLtLNbbMrMSR5eLxL-ZRw_w9kRjFoqLbfW",
#                         "http://www.youtube.com/watch?v=KTNZy8Yxw3I")

# dirty_dancing = media.Movie("Dirty Dancing: Ritmo Quente",
#                         "Na esperança de curtir sua juventude, uma jovem fica decepcionada ao descobrir que seus pais passarão o verão de 1963 com ela em um resort na sonolenta região de Catskills. Mas sua sorte muda quando ela conhece o instrutor de dança do resort, Johnny, um rapaz com um passado bem diferente do dela. Quando ele a coloca como sua nova parceira, os dois acabam se apaixonando. Apesar do pai proibi-la de ver Johnny, ela não dá a mínima.",
#                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtPLAEKWucj_wdeHkpBQ7NqCc7d-c4lDHwAzi8k2OThjhBTe0fqLHbMg",
#                         "http://www.youtube.com/watch?v=g_ptDXkByuQ")

# lord_of_rings = media.Movie("O Senhor dos Anéis",
#                         "O Senhor dos Anéis é uma trilogia cinematográfica dirigida por Peter Jackson com base na obra-prima homónima de J. R. R. Tolkien. Apesar de seguirem a linha-mestra da trilogia, os filmes possuem inserções e desvios com relação ao material original. ",
#                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzLvLRx_k8PmEBIbU40Z41JTnwY5ndR1MTZ1JWiB418RzSBMa2",
#                         "https://www.youtube.com/watch?v=IUerKBZHnBs")

# harry_potter = media.Movie("Harry Potter",
#                         "Conheça Harry Potter, um menino que soube em seu aniversário de onze anos que é filho órfão de dois bruxos e possui poderes mágicos únicos. De filho indesejado, passa a ser um estudante de Hogwarts, uma escola inglesa para bruxos. Lá ele conhece vários amigos que o ajudam a descobrir a verdade sobre as mortes misteriosas de seus pais.",
#                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5-cBOrjWktGZ8ffQIlgOlgz7DpQMiMNb6ZzsGZpKvhRt0zJqe7Q",
#                         "http://www.youtube.com/watch?v=g5NymUQ7edU")

# donnie_darko = media.Movie("Donnie Darko",
#                         "Donnie é um jovem excêntrico que despreza a grande maioria de seus colegas de escola. Ele tem visões, em especial de Frank, um coelho gigante que só ele consegue ver e que o encoraja a fazer brincadeiras humilhantes com quem o cerca. Um dia, uma de suas visões o atrai para fora de casa e lhe diz que o mundo acabará dentro de um mês. Donnie inicialmente não acredita, mas, momentos depois, a turbina de um avião cai em sua casa e ele começa a se perguntar qual é o fundo de verdade dessa previsão.",
#                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6SB-wX_z-U4QS0ikQp499s8rhH1t9dyPXUErqR-HBHKnuV2KqmQ",
#                         "https://www.youtube.com/watch?v=FZZqcmaALJs")


#movies= [avengers_infinity_war, clube_dos_cinco, dirty_dancing, lord_of_rings, harry_potter, donnie_darko]

fresh_tomatoes.open_movies_page(movies)
#print media.Movie.VALID_RATINGS
#print media.Movie.__doc__
#print media.Movie.__name__
#print media.Movie.__module__
