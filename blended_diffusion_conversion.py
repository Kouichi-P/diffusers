# # diffusers/src
#
# from diffusers import UNet2DModel
# import json
#
# with open("ddpm_256_custom_config.json") as fp:
#     config = json.load(fp)
# model = UNet2DModel(**config)
# print(model)
#
# config = dict(model.config)
# print(config)
# print(config["resnet_time_scale_shift"])
#
# exit(0)
# --------------------------------------------------------------------------------
# diffusers/src

from diffusers import UNet2DModel

repo_id = "google/ddpm-church-256"
model = UNet2DModel.from_pretrained(repo_id)
print(type(model.config))

config = dict(model.config)
config["block_out_channels"] = [
    256,
    256,
    512,
    512,
    1024,
    1024,
  ]
config["down_block_types"] = [
    "GuidedDiffusionDownBlock2D",
    "GuidedDiffusionDownBlock2D",
    "GuidedDiffusionDownBlock2D",
    "GuidedDiffusionDownBlock2D",  # attention?
    "GuidedDiffusionDownBlock2D",  # attention?
    "GuidedDiffusionDownBlock2D"   # attention?
]

config["resnet_time_scale_shift"] = "scale_shift"
config["resblock_updown"] = True
model = UNet2DModel(**config)

print(model)
model.save_pretrained("ddpm-church-256-custom")

config = dict(model.config)
print(config)
print(config["resnet_time_scale_shift"])

import json
with open("ddpm_256_custom_config.json", "w") as fp:
   json.dump(config, fp, indent=4)

# --------------------------------------------------------------------------------
# diffusers/src

import torch

ckpt = "ddpm-church-256-custom/diffusion_pytorch_model.bin"
model = torch.load(ckpt)

# print(model)
# print(model.keys())

# for k in model.keys():
#     if k.startswith("time_"):
#         print(k)

info = {k: str(list(v.shape)) for k, v in model.items()}
import json
with open("ddpm_256_custom.json", "w") as fp:
    json.dump(info, fp, indent=4)

exit(0)
# --------------------------------------------------------------------------------
# diffusers/src

import torch

ckpt = "blended-diffusion/256x256_diffusion_uncond.pt"
model = torch.load(ckpt)
# print(model)
# print(model.keys())

# for k in model.keys():
#    if k.startswith("time_embed"):
#        print(k)

info = {k: str(list(v.shape)) for k, v in model.items()}
import json
with open("blended_diffusion.json", "w") as fp:
    json.dump(info, fp, indent=4)
