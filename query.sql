/* Submit to https://data.stackexchange.com/puzzling/query/new to gather data */
/* Data gathered is CC BY-SA 3.0 as of 2018-01-15. */

SELECT TOP 10000
	p.Id, /* Change URL as desired */
	CONCAT('https://puzzling.stackexchange.com/questions/', p.Id) as URL,
	p.Score, p.ViewCount, p.AnswerCount, p.FavoriteCount, p.Title, p.Tags,
	p.Body, p.CreationDate,
	COALESCE(NULLIF(p.OwnerUserId, ''), 0) as OwnerUserId, /* Deleted users */
	COALESCE(NULLIF(pu.DisplayName, ''), 'Anonymous') as DisplayName,
	COALESCE(NULLIF(pu.Reputation, ''), 0) as Reputation,
	COALESCE(NULLIF(pb.Gold, ''), 0) as Gold,
	COALESCE(NULLIF(pb.Silver, ''), 0) as Silver,
	COALESCE(NULLIF(pb.Bronze, ''), 0) as Bronze,
	a.Id as AnswerId, a.Score as AnswerScore,
	a.Body as AnswerBody, a.CreationDate as AnswerCreationDate,
	COALESCE(NULLIF(a.OwnerUserId, ''), 0) as AnswerOwnerId,
	COALESCE(NULLIF(au.DisplayName, ''), 'Anonymous') as AnswerDisplayName,
	COALESCE(NULLIF(au.Reputation, ''), 0) as AnswerReputation,
	COALESCE(NULLIF(ab.Gold, ''), 0) as AnswerGold,
	COALESCE(NULLIF(ab.Silver, ''), 0) as AnswerSilver,
	COALESCE(NULLIF(ab.Bronze, ''), 0) as AnswerBronze
FROM Posts p
INNER JOIN Votes v ON (v.PostId=p.Id)
LEFT JOIN Users pu ON (p.OwnerUserId=pu.Id)
LEFT JOIN (
	SELECT
		UserId,
		COUNT(CASE WHEN Class = 1 THEN 1 END) as Gold,
		COUNT(CASE WHEN Class = 2 THEN 1 END) as Silver,
		COUNT(CASE WHEN Class = 3 THEN 1 END) as Bronze,
		COUNT(*) as Total
	FROM Badges
	GROUP BY UserId
) pb ON (p.OwnerUserId=pb.UserId)
INNER JOIN Posts a ON (a.Id=p.AcceptedAnswerId)
LEFT JOIN Users au ON (a.OwneruserId=au.Id)
LEFT JOIN (
	SELECT
		UserId,
		COUNT(CASE WHEN Class = 1 THEN 1 END) as Gold,
		COUNT(CASE WHEN Class = 2 THEN 1 END) as Silver,
		COUNT(CASE WHEN Class = 3 THEN 1 END) as Bronze,
		COUNT(*) as Total
	FROM Badges
	GROUP BY UserId
) ab ON (a.OwnerUserId=ab.UserId)
WHERE p.PostTypeId = 1 /* Question */
AND p.Score > 0 /* Discard Trash */
GROUP BY
	p.Id, p.Score, p.Title, p.Body, p.CreationDate, p.ViewCount, p.OwnerUserId,
	pu.DisplayName, pu.Reputation, pb.Gold, pb.Silver, pb.Bronze,p.Tags,
	p.AnswerCount, p.FavoriteCount, a.Id, a.Body, a.CreationDate, a.OwnerUserId,
	au.DisplayName, au.Reputation, ab.Gold, ab.Silver, ab.Bronze, a.Score
ORDER BY p.Score Desc
