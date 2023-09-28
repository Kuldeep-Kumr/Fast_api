# Flask API with FastAPI and Airtable Database

## Get All Data - GET Method

- **URL**: http://127.0.0.1:8000/
- **Action**: This endpoint is used to retrieve all user data from your API. When you make a GET request to this URL, the API will return a list of all users' data stored in Airtable.

## Get Specific User Data - GET Method

- **URL**: http://127.0.0.1:8000/user/{user_id}
- **Action**: This endpoint allows you to fetch data for a specific user by providing their `user_id` as a URL parameter. The API will return the user's data corresponding to the given `user_id`.

## Add New User - POST Method

- **URL**: http://127.0.0.1:8000/adduser
- **Action**: To add a new user to your system, you need to make a POST request to this URL. The request body should contain the user's information, including name, phone, email, and address. Upon successful addition, the API will respond confirming the user has been added with user's data and a unique id.

## Update Specific User Data - PATCH Method

- **URL**: http://127.0.0.1:8000/user/{user_id}
- **Action**: To update the data of a specific user, you should make a PATCH request to this URL, including the `user_id` of the user whose data you want to update. In the request body, provide the new data or the fields you want to modify. The API will update the user's data accordingly and return the response of the updated user data.

## Delete Specific User - DELETE Method

- **URL**: http://127.0.0.1:8000/user/{user_id}
- **Action**: To remove a specific user from your system, send a DELETE request to this URL with the `user_id` as a parameter. The API will delete the user's data associated with the provided `user_id`.

To run the code, add your Airtable Base ID, TableName, and Token. Then further run the command `uvicorn main:app --reload`. It will start the server on localhost.
