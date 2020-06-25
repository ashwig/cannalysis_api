DROP TABLE IF EXISTS metrc_resp;
DROP TABLE IF EXISTS metrc_reqs;
CREATE TABLE metrc_reqs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    request_string TEXT NOT NULL
);
CREATE TABLE metrc_resps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    result_code INTEGER NOT NULL,
    license_facility TEXT NOT NULL,
    id_number TEXT NOT NULL,
    last_modified_date TIMESTAMP NOT NULL,
    tag_number TEXT NOT NULL,
    request_string TEXT NOT NULL,
    json_body TEXT NOT NULL,
    created TIMESTAMP NOT NULL,
    FOREIGN KEY (request_string) REFERENCES metrc_reqs (request_string),
    FOREIGN KEY (created) REFERENCES metrc_reqs (created)
);