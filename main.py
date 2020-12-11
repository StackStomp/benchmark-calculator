# -*- coding: utf-8 -*-

from wox import FlowLauncher
import calc


class HelloWorld(FlowLauncher):

    def query(self, query):
        results = []
        try:
            arg = calc.CalcArg.from_query(query)
        except calc.ParseError as e:
            results.append({
                "Title": "Invalid number",
                "SubTitle": e.message,
                "IcoPath":"Images/app.png",
                "ContextData": "ctxData"
            })
            return results

        if arg.none_num() > 1:
            results.append({
                "Title": "Benchmark data converter",
                "SubTitle": "Batch, Rank, FPS, StepTime, Get 3, calc 1",
                "IcoPath":"Images/app.png",
                "ContextData": "ctxData"
            })
            return results

        if arg.none_num() == 1:
            if arg.step_time is None:
                results.append({
                    "Title": "StepTime = 1 / (FPS / rank / batch)",
                    "SubTitle": "StepTime: {}".format(calc.calc_step_time(arg)),
                    "IcoPath": "Images/app.png",
                    "ContextData": "ctxData"
                })
                return results
            if arg.fps is None:
                results.append({
                    "Title": "FPS = 1 / StepTime * rank * batch",
                    "SubTitle": "FPS: {}".format(calc.calc_fps(arg)),
                    "IcoPath": "Images/app.png",
                    "ContextData": "ctxData"
                })
                return results
            if arg.rank is None:
                results.append({
                    "Title": "Rank = FPS * StepTime / Batch",
                    "SubTitle": "Rank: {}".format(calc.calc_rank(arg)),
                    "IcoPath": "Images/app.png",
                    "ContextData": "ctxData"
                })
                return results
            if arg.batch is None:
                results.append({
                    "Title": "Batch = FPS * StepTime / Rank",
                    "SubTitle": "Batch: {}".format(calc.calc_batch(arg)),
                    "IcoPath": "Images/app.png",
                    "ContextData": "ctxData"
                })
                return results

        results.append({
            "Title": "Not support Yet",
            "SubTitle": "Query: {}".format(query),
            "IcoPath":"Images/app.png",
            "ContextData": "ctxData"
        })
        return results


if __name__ == "__main__":
    HelloWorld()