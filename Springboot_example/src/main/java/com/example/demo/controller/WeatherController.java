package com.example.demo.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.HttpSessionRequiredException;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.print.DocFlavor;
import javax.servlet.http.HttpServletRequest;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;

@Controller
public class WeatherController {
    @GetMapping(value = "/weather")
    @ResponseBody
    public String weather(HttpServletRequest request) throws Exception {
        String city = request.getParameter("city");
        String html = sendGet("https://m.search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8+" + URLEncoder.encode(city, "UTF-8"));

        html = html.split("현재 온도")[1].split("report_card_wrap")[0];
        String cel = html.split("<span class=\"celsius")[0].replace("</span>", "");
        String status = html.split("<br>")[1].split("</p")[0];
        String msg = cel + "도이며, " + status + "입니다.";
        return msg;
    }

    private String sendGet(String targetUrl) throws Exception {
        URL url = new URL(targetUrl);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("User-Agent", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36");
        int responseCode = con.getResponseCode();
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();
        return response.toString();

    }


}

