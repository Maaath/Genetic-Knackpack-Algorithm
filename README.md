<h1>:briefcase: Genetic Knackpack Algorithm</h1>

<div style="display: inline_block">
 <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" />
 <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" />  
</div>

<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/38335297/161128378-f9ed21d2-f1c2-474f-a461-4ac36edd6453.png" width="300px;" alt="Math Picture"/>
</div>

<br>

<div style="display: inline_block"> 
 <a href = "mailto:macedo.matheus81@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
 <a href="https://www.linkedin.com/in/math-macedo/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
 <a href="https://matheus-macedo.herokuapp.com/"><img src="https://img.shields.io/badge/-Portf%C3%B3lio-brown?style=for-the-badge&logo=true" target="_blank"></a> 
</div>

<h2>:page_with_curl: Description</h2>
<p>The purpose of the algorithm is converge to the objective.</p>

<h2>:handbag: Knackpack Problem</h2>
<p>The Knackpack problem is a combinatorial optimization problem: given a set of items, each with a weight and a value, we must determine which item to include in a collection (Knackpack) so the total weight is less than or equal to a certain limit and the total amount is as large as possible. The problem's name derives from the problem faced by someone who has a fixed-size Knackpack and must fill it with the most valuable items. The problem usually arises in resource allocation, where the algorithm has to choose between a set of non-divisible projects or tasks under a fixed budget (weight) or time constraint, respectively.
The knapsack problem has been studied for over a century, with the earliest work dating back to 1897. The name "knapsack problem" dates back to the early work of mathematician Tobias Danzig (1884–1956), and refers to the common problem of packing more valuable or useful items without overloading your luggage.</p>

<h2>:space_invader: Genetic Algorithms</h2>
<p>Based on Darwin's theory that says "The better an individual adapts to its environment, the greater its chance to surviving and generating offspring", the idea of genetic algorithms is based on seeking to create a new stronger generation, ideal among others characteristics, if compared with the ancestors.
There are many ways to apply this concept, but regardless of application, in general it can be said that according to a certain objective, a population, that is, countless possible solutions, can be related, becoming “parents” and from that make the genetic alteration, that is, take characteristics of these parents and put them in the next generation with the objective that this new group of individuals have greater capacity to reach a better solution, that is, with greater probability of adapting to the environment.</p>

<h2>:memo: Methodology</h2>
<h3>:ferris_wheel: Roulette wheel selection </h3>
<p>This method, like others, seeks to give chances to individuals who, although they may not have very good genetics, may have good characteristics, but in order for this individual to be a father to generate new children, in the case of roulette, this must be decided by means of luck using a roulette wheel. The operation if a draw by roulette consists of spinning a roulette, a fixed arrow that points to a part of the roulette indicates which part is selected, and in genetic algorithms, the selected parts refer to the individuals who will be the parents of the next generation , but the chances of winning are not equal for all individuals in the population, so, to have a greater chance of a possible father with better genes to win, he has a greater area on the roulette wheel, this area being proportional to the probability that he is the best gene, making there a greater chance of being drawn.</p>


<h2>:dart: Results</h2>
<h3>Constants</h3>
<li>We used retain=0.2 to select 20% to become parents</li>
<li>random_select=0.05 to select 5% randomly to promote genetic diversity</li>
<li> and finally mutate=0.01 to mutate 1%</li>
<br>
<div align="center">
 <img src="https://user-images.githubusercontent.com/38335297/161145671-2bf1e582-7130-4826-8103-68f99ed1b80d.PNG" width="900px;" alt="Constants Picture"/><br>
</div>
<h3>Low complexity (4 itens, 20 epochs and limit 5kg)</h3>
<h4>Parameters:</h4>
<div align="center">
 <img src="https://user-images.githubusercontent.com/38335297/161148975-39d2ccee-7f96-4ee0-b1d9-1e62307ee0ac.PNG" width="900px;" alt="Constants Picture"/><br>
</div>
<h4>Out:</h4>
<p>We can see that after two epochs it already reaches the goal, which is the value 37.</p>
<div>
 <img src="https://user-images.githubusercontent.com/38335297/161149272-ba171a33-c5de-4d68-b69e-4b8742324a50.PNG" width="100px;" style="margin-left:10%; alt="Constants Picture"/>
</div>

<h2>:wrench: Credits</h2>
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Maaath">
        <img src="https://user-images.githubusercontent.com/38335297/161117931-699ddbe5-7e53-45cb-a834-bcb3bb48eb10.png" width="100px;" alt="Math Picture"/><br>
        <sub>
          <b>Matheus Macedo</b>
        </sub>
      </a>
    </td>
   <td align="center">
      <a href="https://github.com/AlvesMaickel">
        <img src="https://user-images.githubusercontent.com/38335297/161131639-e629a031-c380-4c42-9753-dafd084bacdd.png" width="95px;" alt="Maickel Picture"/><br>
        <sub>
          <b>Maickel Alves</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h2>:moneybag: License</h2>
<b>All rights reserved</b>
