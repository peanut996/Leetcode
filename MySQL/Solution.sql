CREATE Table IF NOT EXISTS`BLACK_INFO`(
  ID INT NOT NULL AUTO_INCRE,
  consumer_id bigint NOT NULL,
  consumer_type int NOT NULL,
  consumer_name varchar(255) NOT NULL,
  certificate_type int NOT NULL,
  certificate_number varchar(255) not NULL,
  block_reason varchar(255),
  info_from varchar(255),
  primary key (`consumer_id`),
)

delete from `BLACK_INFO` 
where 
  1=1 
and 
  certificate_number = 'xxx' 
and 
  block_reason = '反洗钱'

ALTER Table `BLACK_INFO` modify column block_reason varchar(100);

