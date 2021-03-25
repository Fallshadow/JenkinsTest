using System.Collections;
using System.IO;
using UnityEditor;
using UnityEngine;
using System.Collections.Generic;
using System;

public class BuildingUtility : Editor 
{
    enum BuildQuality
    {
        VeryLow,
        Low,
        Medium,
        High,
        VeryHigh,
        Utral,
    }

    const BuildQuality QUALITY_FOR_WINDOWS = BuildQuality.Utral;
    const BuildQuality QUALITY_FOR_ANDROID = BuildQuality.High;
    const BuildQuality QUALITY_FOR_IPHONE = BuildQuality.High;
        //shell脚本直接调用这个静态方法    
    [MenuItem("Version/Windows/Build Windows")]
    static void BuildWindows()
    {
        var now = System.DateTime.Now;
        string nowstr = string.Format("{0:0000}.{1:00}.{2:00}-{3:00}.{4:00}.{5:00}", now.Year, now.Month, now.Day, now.Hour, now.Minute, now.Second);
        BuildWindowWithName(nowstr);
    }

    static void BuildWindowWithName(string pathName)
    {
        QualitySettings.SetQualityLevel((int)QUALITY_FOR_WINDOWS);
        QualitySettings.skinWeights = SkinWeights.Unlimited;

        EditorUserBuildSettings.development = false;
        EditorUserBuildSettings.connectProfiler = false;

        string path = Application.dataPath + "/../../" + "ACT_PC_" + pathName;
        Directory.CreateDirectory(path);
        string strPathexe = path + "/ACT.exe";
        string[] scenes = null;
        BuildPipeline.BuildPlayer(scenes, strPathexe, BuildTarget.StandaloneWindows64, BuildOptions.Development | BuildOptions.ConnectWithProfiler | BuildOptions.EnableDeepProfilingSupport);    }
}