response_json_base={
        "type": "object",
        "properties": {
        "eqt_cat_code": {
            "type": "string"
        },
        "eqt_cat_descr": {
            "type": "string"
        },
        "eqt_cat_id": {
            "type": "string"
        },
        "eqt_code": {
            "type": "string"
        },
        "eqt_db_id": {
            "type": "string"
        },
        "eqt_end_date": {
            "type": "string",
            "format": "date"
        },
        "eqt_end_date_timestamp": {
            "type": "integer",
            "format": "int64"
        },
        "eqt_grp_code": {
            "type": "string"
        },
        "eqt_grp_descr": {
            "type": "string"
        },
        "eqt_grp_id": {
            "type": "string"
        },
        "eqt_name": {
            "type": "string"
        },
        "eqt_name_past": {
            "type": "string"
        },
        "eqt_type_code": {
            "type": "string"
        },
        "eqt_type_descr": {
            "type": "string"
        },
        "eqt_type_id": {
            "type": "string"
        },
        "ownequipment": {
            "type": "integer"
        }
        }
    }
response_json={
        "allOf": [
          {
            "type": "object",
        "properties": {
        "eqt_cat_code": {
            "type": "string"
        },
        "eqt_cat_descr": {
            "type": "string"
        },
        "eqt_cat_id": {
            "type": "string"
        },
        "eqt_code": {
            "type": "string"
        },
        "eqt_db_id": {
            "type": "string"
        },
        "eqt_end_date": {
            "type": "string",
            "format": "date"
        },
        "eqt_end_date_timestamp": {
            "type": "integer",
            "format": "int64"
        },
        "eqt_grp_code": {
            "type": "string"
        },
        "eqt_grp_descr": {
            "type": "string"
        },
        "eqt_grp_id": {
            "type": "string"
        },
        "eqt_name": {
            "type": "string"
        },
        "eqt_name_past": {
            "type": "string"
        },
        "eqt_type_code": {
            "type": "string"
        },
        "eqt_type_descr": {
            "type": "string"
        },
        "eqt_type_id": {
            "type": "string"
        },
        "ownequipment": {
            "type": "integer"
        }
        }
          },
          {
            "type": "object",
            "properties": {
              "properties": {
                "type": "object"
              }
            }
          }
        ]
      }