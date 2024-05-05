package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

type BaseballResult struct {
	Flag   string
	LTeam  string
	LScore string
	RScore string
	RTeam  string
}

func getBaseball() string {
	url := "https://www.koreabaseball.com/Schedule/ScoreBoard.aspx"
	response, err := http.Get(url)
	if err != nil {
		log.Fatal(err)
	}
	defer response.Body.Close()

	doc, err := goquery.NewDocumentFromReader(response.Body)
	if err != nil {
		log.Fatal(err)
	}

	results := make([]BaseballResult, 0)

	doc.Find("#cphContents_cphContents_cphContents_udpRecord .leftTeam").Each(func(i int, s *goquery.Selection) {
		lScore := s.Find("em.score").Text()
		lTeam := s.Find("strong.teamT").Text()

		result := BaseballResult{
			LTeam:  lTeam,
			LScore: lScore,
		}
		results = append(results, result)
	})

	doc.Find("strong.flag").Each(func(i int, s *goquery.Selection) {
		flag := s.Text()
		results[i].Flag = flag
	})

	doc.Find("#cphContents_cphContents_cphContents_udpRecord .rightTeam").Each(func(i int, s *goquery.Selection) {
		rScore := s.Find("em.score").Text()
		rTeam := s.Find("strong.teamT").Text()

		results[i].RScore = rScore
		results[i].RTeam = rTeam
	})

	var msgs []string
	for _, result := range results {
		msg := fmt.Sprintf("%s    %s %s : %s %s", result.Flag, result.LTeam, result.LScore, result.RScore, result.RTeam)
		msgs = append(msgs, msg)
	}
	return strings.Join(msgs, "\n")
}

func main() {
	msg := getBaseball()
	fmt.Println(msg)
}
