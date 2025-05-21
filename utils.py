import pandas as pd

# chunk the content field of df into 500 tokens, returning a new df with the chunked content
def chunk_content(in_df, chunk_size=500):
    new_df = pd.DataFrame()
    for index, row in in_df.iterrows():
        content = row["content"]
        chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
        chunk_ids = range(0, len(chunks))
        for chunk, chunk_id in zip(chunks, chunk_ids):
            new_fields = {"content": chunk, "chunk_id": chunk_id}
            old_fields = row.to_dict()
            old_fields.pop("content", None)
            new_row = {**new_fields, **old_fields}
            new_df = pd.concat([new_df, pd.DataFrame([new_row])])
        new_df.reset_index(drop=True, inplace=True)
    return new_df
