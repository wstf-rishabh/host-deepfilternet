from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
import uuid
import shutil
from denoise import denoise_audio

app = FastAPI()

UPLOAD_DIR = Path("audio_uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/denoise/")
async def upload_audio(file: UploadFile = File(...)):
    try:
        # Sanitize filename
        safe_filename = Path(file.filename).name
        input_path = UPLOAD_DIR / f"{uuid.uuid4()}_{safe_filename}"
        output_path = input_path.with_name(input_path.stem + "_denoised.wav")

        # Save uploaded file
        with open(input_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Denoise
        denoise_audio(str(input_path), str(output_path))

        # Return the denoised file directly
        return FileResponse(
            path=output_path,
            media_type="audio/wav",
            filename=output_path.name
        )

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse({"error": str(e)}, status_code=500)
