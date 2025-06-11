package com.dietfit.service.spoonacular.api

import com.dietfit.exception.ClientException
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.Path
import retrofit2.http.POST
import retrofit2.http.Query
import arrow.core.Either
import com.dietfit.service.spoonacular.model.AnalyzeRecipeRequest
import com.dietfit.service.spoonacular.model.SearchRestaurants200Response

interface DefaultService {
  /**
   * POST recipes/analyze
   * Analyze Recipe
   * This endpoint allows you to send raw recipe information, such as title, servings, and ingredients, to then see what we compute (badges, diets, nutrition, and more). This is useful if you have your own recipe data and want to enrich it with our semantic analysis.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param analyzeRecipeRequest Example request body.
   * @param language The input language, either \"en\" or \"de\". (optional)
   * @param includeNutrition Whether nutrition data should be added to correctly parsed ingredients. (optional)
   * @param includeTaste Whether taste data should be added to correctly parsed ingredients. (optional)
   * @return Either<kotlin.Any, ClientException>
   */
  @POST("recipes/analyze")
  suspend fun analyzeRecipe(@Body analyzeRecipeRequest: AnalyzeRecipeRequest, @Query("language") language: kotlin.String? = null, @Query("includeNutrition") includeNutrition: kotlin.Boolean? = null, @Query("includeTaste") includeTaste: kotlin.Boolean? = null): Either<kotlin.Any, ClientException>

  /**
   * GET recipes/{id}/card
   * Create Recipe Card
   * Generate a recipe card for a recipe.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param id The recipe id.
   * @param mask The mask to put over the recipe image (\"ellipseMask\", \"diamondMask\", \"starMask\", \"heartMask\", \"potMask\", \"fishMask\"). (optional)
   * @param backgroundImage The background image (\"none\",\"background1\", or \"background2\"). (optional)
   * @param backgroundColor The background color for the recipe card as a hex-string. (optional)
   * @param fontColor The font color for the recipe card as a hex-string. (optional)
   * @return Either<kotlin.Any, ClientException>
   */
  @GET("recipes/{id}/card")
  suspend fun createRecipeCardGet(@Path("id") id: kotlin.Int, @Query("mask") mask: kotlin.String? = null, @Query("backgroundImage") backgroundImage: kotlin.String? = null, @Query("backgroundColor") backgroundColor: kotlin.String? = null, @Query("fontColor") fontColor: kotlin.String? = null): Either<kotlin.Any, ClientException>

  /**
   * GET food/restaurants/search
   * Search Restaurants
   * Search through thousands of restaurants (in North America) by location, cuisine, budget, and more.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param query The search query. (optional)
   * @param lat The latitude of the user's location. (optional)
   * @param lng The longitude of the user's location. (optional)
   * @param distance The distance around the location in miles. (optional)
   * @param budget The user's budget for a meal in USD. (optional)
   * @param cuisine The cuisine of the restaurant. (optional)
   * @param minRating The minimum rating of the restaurant between 0 and 5. (optional)
   * @param isOpen Whether the restaurant must be open at the time of search. (optional)
   * @param sort How to sort the results, one of the following 'cheapest', 'fastest', 'rating', 'distance' or the default 'relevance'. (optional)
   * @param page The page number of results. (optional)
   * @return Either<SearchRestaurants200Response, ClientException>
   */
  @GET("food/restaurants/search")
  suspend fun searchRestaurants(@Query("query") query: kotlin.String? = null, @Query("lat") lat: java.math.BigDecimal? = null, @Query("lng") lng: java.math.BigDecimal? = null, @Query("distance") distance: java.math.BigDecimal? = null, @Query("budget") budget: java.math.BigDecimal? = null, @Query("cuisine") cuisine: kotlin.String? = null, @Query("min-rating") minRating: java.math.BigDecimal? = null, @Query("is-open") isOpen: kotlin.Boolean? = null, @Query("sort") sort: kotlin.String? = null, @Query("page") page: java.math.BigDecimal? = null): Either<SearchRestaurants200Response, ClientException>
}
