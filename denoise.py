from df.enhance import enhance, init_df, load_audio, save_audio
from pathlib import Path

def denoise_audio(input_path: str, output_path: str):
    model, df_state, _ = init_df()
    audio, _ = load_audio(input_path, sr=df_state.sr())
    enhanced = enhance(model, df_state, audio)
    save_audio(output_path, enhanced, df_state.sr())
    return output_path

# CLI test
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Denoise audio using DeepFilterNet")
    parser.add_argument("input", help="Path to input audio file")
    parser.add_argument("output", nargs="?", help="Path to save denoised output")

    args = parser.parse_args()
    input_path = args.input
    output_path = args.output or str(Path(input_path).with_name(Path(input_path).stem + "_denoised.wav"))

    print(f"Denoising: {input_path}")
    try:
        result_path = denoise_audio(input_path, output_path)
        print(f"Denoised file saved at: {result_path}")
    except Exception as e:
        print(f"❌ Error: {e}")
