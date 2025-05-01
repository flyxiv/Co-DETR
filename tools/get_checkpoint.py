from huggingface_hub import hf_hub_download

# 모델 파일 다운로드
checkpoint_path = hf_hub_download(
    repo_id="zongzhuofan/co-detr-vit-large-coco-instance",
    filename="pytorch_model.pth",
    local_dir="./checkpoints"
)

print(f"model downloaded to {checkpoint_path}")