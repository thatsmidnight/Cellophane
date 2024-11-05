# Cellophane

## User Stories

### I. Abstract Base Class & Class Mixin

1. As a developer, I want to create an abstract base class for API wrappers so that I can define a common structure and interface for all API interactions.
   - The abstract base class should have an `__init__` method that takes the API key and any other necessary parameters as input.
   - The `__init__` method should authenticate the client and store the authentication token in a class attribute.
   - The abstract base class should have abstract methods for `.get`, `.post`, `.put`, `.patch`, and `.delete` to enforce a consistent interface for all API wrappers.

2. As a developer, I want to create a class mixin that uses the `requests` library so that I can easily make HTTP requests to external APIs.
   - The class mixin should have methods for making `.get`, `.post`, `.put`, `.patch`, and `.delete` requests.
   - These methods should take the endpoint URL and any necessary parameters as input.
   - These methods should handle common request headers, such as authorization and content type.
   - These methods should return the response from the API call in a standardized format.

3. As a developer, I want to integrate the class mixin with the abstract base class so that I can make API calls with authentication.
   - The abstract base class should inherit from the class mixin.
   - The abstract methods in the base class should use the methods from the mixin to make API calls.
   - The base class should handle authentication by including the authentication token in the request headers.

4. As a developer, I want to implement automatic re-authentication in the abstract base class so that API calls do not fail due to expired tokens.
   - The abstract base class should detect when an API call fails due to authentication issues.
   - The base class should re-authenticate the client and obtain a new token.
   - The base class should retry the failed API call with the new token.

5. As a developer, I want to add error handling to the abstract base class and class mixin so that I can gracefully handle API exceptions.
   - The methods in the mixin and base class should handle common API exceptions, such as network errors and API rate limits.
   - The methods should provide informative error messages and log the exceptions.
   - The methods should allow for custom exception handling by the concrete API classes.
