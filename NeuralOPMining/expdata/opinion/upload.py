# huggingface-cli login
# guide: https://zhuanlan.zhihu.com/p/564816807
from huggingface_hub import create_repo

repo_url = create_repo(name="mpqa", repo_type="dataset")

from huggingface_hub import Repository

repo = Repository(local_dir="mpqa", clone_from=repo_url)
!cp issues-datasets-with-hf-doc-builder.jsonl github-issues/

repo.lfs_track("*.jsonl")   

repo.push_to_hub()
