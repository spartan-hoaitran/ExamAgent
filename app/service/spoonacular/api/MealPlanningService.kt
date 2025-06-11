package com.dietfit.service.spoonacular.api

import com.dietfit.exception.ClientException
import retrofit2.http.Body
import retrofit2.http.DELETE
import retrofit2.http.GET
import retrofit2.http.Path
import retrofit2.http.POST
import retrofit2.http.Query
import arrow.core.Either
import com.dietfit.service.spoonacular.model.AddMealPlanTemplate200Response
import com.dietfit.service.spoonacular.model.AddToMealPlanRequest
import com.dietfit.service.spoonacular.model.AddToShoppingListRequest
import com.dietfit.service.spoonacular.model.ConnectUser200Response
import com.dietfit.service.spoonacular.model.ConnectUserRequest
import com.dietfit.service.spoonacular.model.GenerateMealPlan200Response
import com.dietfit.service.spoonacular.model.GetMealPlanTemplate200Response
import com.dietfit.service.spoonacular.model.GetMealPlanTemplates200Response
import com.dietfit.service.spoonacular.model.GetMealPlanWeek200Response
import com.dietfit.service.spoonacular.model.GetShoppingList200Response

interface MealPlanningService {
  /**
   * POST mealplanner/{username}/templates
   * Add Meal Plan Template
   * Add a meal plan template for a user.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @return Either<AddMealPlanTemplate200Response, ClientException>
   */
  @POST("mealplanner/{username}/templates")
  suspend fun addMealPlanTemplate(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String): Either<AddMealPlanTemplate200Response, ClientException>

  /**
   * POST mealplanner/{username}/items
   * Add to Meal Plan
   * Add an item to the user's meal plan.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @param addToMealPlanRequest
   * @return Either<kotlin.Any, ClientException>
   */
  @POST("mealplanner/{username}/items")
  suspend fun addToMealPlan(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String, @Body addToMealPlanRequest: AddToMealPlanRequest): Either<kotlin.Any, ClientException>

  /**
   * POST mealplanner/{username}/shopping-list/items
   * Add to Shopping List
   * Add an item to the user's shopping list.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @param addToShoppingListRequest
   * @return Either<kotlin.Any, ClientException>
   */
  @POST("mealplanner/{username}/shopping-list/items")
  suspend fun addToShoppingList(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String, @Body addToShoppingListRequest: AddToShoppingListRequest): Either<kotlin.Any, ClientException>

  /**
   * POST mealplanner/{username}/connect
   * Connect User
   * Connect a user to the meal planning service.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @param connectUserRequest
   * @return Either<ConnectUser200Response, ClientException>
   */
  @POST("mealplanner/{username}/connect")
  suspend fun connectUser(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String, @Body connectUserRequest: ConnectUserRequest): Either<ConnectUser200Response, ClientException>

  /**
   * GET mealplanner/{username}/templates
   * Get Meal Plan Templates
   * Get all meal plan templates for a user.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @return Either<GetMealPlanTemplates200Response, ClientException>
   */
  @GET("mealplanner/{username}/templates")
  suspend fun getMealPlanTemplates(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String): Either<GetMealPlanTemplates200Response, ClientException>

  /**
   * GET mealplanner/{username}/template/{id}
   * Get Meal Plan Template
   * Get a specific meal plan template by ID.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @param id The ID of the meal plan template.
   * @return Either<GetMealPlanTemplate200Response, ClientException>
   */
  @GET("mealplanner/{username}/template/{id}")
  suspend fun getMealPlanTemplate(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String, @Path("id") id: kotlin.String): Either<GetMealPlanTemplate200Response, ClientException>

  /**
   * GET mealplanner/{username}/week/{year}-{week}
   * Get Meal Plan Week
   * Get the meal plan for a specific week.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @param year The year of the meal plan.
   * @param week The week number.
   * @return Either<GetMealPlanWeek200Response, ClientException>
   */
  @GET("mealplanner/{username}/week/{year}-{week}")
  suspend fun getMealPlanWeek(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String, @Path("year") year: kotlin.String, @Path("week") week: kotlin.String): Either<GetMealPlanWeek200Response, ClientException>

  /**
   * GET mealplanner/{username}/shopping-list
   * Get Shopping List
   * Get the user's shopping list.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @return Either<GetShoppingList200Response, ClientException>
   */
  @GET("mealplanner/{username}/shopping-list")
  suspend fun getShoppingList(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String): Either<GetShoppingList200Response, ClientException>

  /**
   * DELETE mealplanner/{username}/items/{id}
   * Delete from Meal Plan
   * Remove an item from the user's meal plan.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @param id The ID of the item to remove.
   * @return Either<kotlin.Any, ClientException>
   */
  @DELETE("mealplanner/{username}/items/{id}")
  suspend fun deleteFromMealPlan(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String, @Path("id") id: kotlin.String): Either<kotlin.Any, ClientException>

  /**
   * DELETE mealplanner/{username}/shopping-list/items/{id}
   * Delete from Shopping List
   * Remove an item from the user's shopping list.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @param id The ID of the item to remove.
   * @return Either<kotlin.Any, ClientException>
   */
  @DELETE("mealplanner/{username}/shopping-list/items/{id}")
  suspend fun deleteFromShoppingList(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String, @Path("id") id: kotlin.String): Either<kotlin.Any, ClientException>

  /**
   * DELETE mealplanner/{username}/templates/{id}
   * Delete Meal Plan Template
   * Remove a meal plan template.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @param id The ID of the template to remove.
   * @return Either<kotlin.Any, ClientException>
   */
  @DELETE("mealplanner/{username}/templates/{id}")
  suspend fun deleteMealPlanTemplate(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String, @Path("id") id: kotlin.String): Either<kotlin.Any, ClientException>

  /**
   * DELETE mealplanner/{username}/week/{year}-{week}
   * Delete Meal Plan Week
   * Remove a meal plan for a specific week.
   * Responses:
   *  - 200: Success
   *  - 401: Unauthorized
   *  - 403: Forbidden
   *  - 404: Not Found
   *
   * @param username The username.
   * @param hash The private hash for the username.
   * @param year The year of the meal plan.
   * @param week The week number.
   * @return Either<kotlin.Any, ClientException>
   */
  @DELETE("mealplanner/{username}/week/{year}-{week}")
  suspend fun deleteMealPlanWeek(@Path("username") username: kotlin.String, @Query("hash") hash: kotlin.String, @Path("year") year: kotlin.String, @Path("week") week: kotlin.String): Either<kotlin.Any, ClientException>
}
