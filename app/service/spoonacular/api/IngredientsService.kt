package com.dietfit.service.spoonacular.api

import com.dietfit.exception.ClientException
import retrofit2.http.Body
import retrofit2.http.Field
import retrofit2.http.FormUrlEncoded
import retrofit2.http.GET
import retrofit2.http.Path
import retrofit2.http.POST
import retrofit2.http.Query
import arrow.core.Either
import okhttp3.ResponseBody
import com.fasterxml.jackson.annotation.JsonProperty
import com.dietfit.service.spoonacular.model.AutocompleteIngredientSearch200ResponseInner
import com.dietfit.service.spoonacular.model.ComputeIngredientAmount200Response
import com.dietfit.service.spoonacular.model.GetIngredientSubstitutes200Response
import com.dietfit.service.spoonacular.model.IngredientInformation
import com.dietfit.service.spoonacular.model.IngredientSearch200Response
import com.dietfit.service.spoonacular.model.MapIngredientsToGroceryProducts200ResponseInner
import com.dietfit.service.spoonacular.model.MapIngredientsToGroceryProductsRequest

interface IngredientsService {

  /**
   * enum for parameter language
   */
  enum class LanguageAutocompleteIngredientSearch(val value: kotlin.String) {
    @JsonProperty(value = "en")
    EN("en"),

    @JsonProperty(value = "de")
    DE("de")
  }

  /**
   * GET food/ingredients/autocomplete
   * Autocomplete Ingredient Search
   * Autocomplete the entry of an ingredient.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param query The (natural language) search query.
   * @param number The maximum number of items to return (between 1 and 100). Defaults to 10. (optional, default to 10)
   * @param metaInformation Whether to return more meta information about the ingredients. (optional)
   * @param intolerances A comma-separated list of intolerances. All recipes returned must not contain ingredients that are not suitable for people with the intolerances entered. See a full list of supported intolerances. (optional)
   * @param language The language of the input. Either 'en' or 'de'. (optional)
   * @return Either<kotlin.collections.Set<AutocompleteIngredientSearch200ResponseInner>, ClientException>
   */
  @GET("food/ingredients/autocomplete")
  suspend fun autocompleteIngredientSearch(@Query("query") query: kotlin.String, @Query("number") number: kotlin.Int? = 10, @Query("metaInformation") metaInformation: kotlin.Boolean? = null, @Query("intolerances") intolerances: kotlin.String? = null, @Query("language") language: LanguageAutocompleteIngredientSearch? = null): Either<kotlin.collections.Set<AutocompleteIngredientSearch200ResponseInner>, ClientException>

  /**
   * GET food/ingredients/{id}/amount
   * Compute Ingredient Amount
   * Compute the amount you need of a certain ingredient for a certain nutritional goal. For example, how much pineapple do you have to eat to get 10 grams of protein?
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param id The id of the ingredient you want the amount for.
   * @param nutrient The target nutrient. See a list of supported nutrients.
   * @param target The target number of the given nutrient.
   * @param unit The target unit. (optional)
   * @return Either<ComputeIngredientAmount200Response, ClientException>
   */
  @GET("food/ingredients/{id}/amount")
  suspend fun computeIngredientAmount(@Path("id") id: kotlin.Int, @Query("nutrient") nutrient: kotlin.String, @Query("target") target: kotlin.Int, @Query("unit") unit: kotlin.String? = null): Either<ComputeIngredientAmount200Response, ClientException>
}
