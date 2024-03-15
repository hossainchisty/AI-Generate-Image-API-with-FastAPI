# AI Generate Image API with FastAPI

This is a simple API built with FastAPI that allows users to generate images using AI models. It provides endpoints to generate images based on various prompts or text descriptions. This README will guide you through setting up and using the API effectively.

## Installation

To install and run the API, follow these steps:

1. Clone this repository:

   ```
   git clone https://github.com/hossainchisty/AI-Generate-Image-API-with-FastAPI.git
   ```

2. Navigate into the cloned directory:

   ```
   cd AI-Generate-Image-API-with-FastAPI
   ```

3. Install the dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:

   ```
   uvicorn main:app --reload
   ```

The API server should now be running locally on `http://localhost:8000`.

## Usage

### Generating Images

#### Endpoint: `/generate-image`

- **Method:** POST
- **Description:** Generates an image based on the provided prompt.
- **Request Body:**
  - `prompt`: String - Text prompt or description for generating the image.
- **Response:**
  - `image`: Binary - The generated image in PNG format.

Example using cURL:

```bash
curl -X POST "http://localhost:8000/generate-image" -H "Content-Type: application/json" -d '{"prompt":"A cat sitting on a tree branch"}' --output generated_image.png
```

### Health Check

#### Endpoint: `/health`

- **Method:** GET
- **Description:** Checks if the API server is running.
- **Response:** "API is running" if the server is active.

Example using cURL:

```bash
curl -X GET "http://localhost:8000/health"
```

## Contributions

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
